from django.http.response import JsonResponse
import requests
from requests.models import HTTPBasicAuth
from common.Exceptions import TokenNull
from spotifyservice.utils import generateTopTracksResponse, getRandomArtistByGenre, getRequestHeader, sortArtistsByPopularity
from suggesty.settings import SPOTIFY_API_URL, SPOTIFY_CLIENTID, SPOTIFY_CLIENTSECRET

#TODO Abstraction
class SpotifyService:
    __requestToken = None

    def __init__(self):
        self.__getSpotifyToken()

    def testSpotifyToken(self):
        return requests.post(f"https://accounts.spotify.com/api/token",auth=HTTPBasicAuth(SPOTIFY_CLIENTID,SPOTIFY_CLIENTSECRET),data={"grant_type": "client_credentials"})

    #Gets OAuth2 token for requests, since this flow has no refresh token, had to control its validation with exceptions and response codes to refresh it.
    def __getSpotifyToken(self):
        print("Spotify OAuth2 token generated")
        self.__requestToken = requests.post(f"https://accounts.spotify.com/api/token",auth=HTTPBasicAuth(SPOTIFY_CLIENTID,SPOTIFY_CLIENTSECRET),data={"grant_type": "client_credentials"}).json()
        return self.__requestToken

    #Selects random artist based on given genre from static object, search artist on spotify, returns result of found artists with given name.
    def __searchRandomArtistByGenre(self,genre):
        try:
            #Token check
            if self.__requestToken is None:
                print("Search artist: Spotify token is null, creating one.")
                self.__getSpotifyToken()

            #Did we found any artist related to given genre in static "list"(dict)
            isFound, selectedArtist = getRandomArtistByGenre(genre)
            if not isFound:#if genre not exist
                return (False,{"RESULT":"Given genre not covered by this application."})
            
            #Search with found artist/band name on spotify, might return similar&multiple results so we need to pick right one
            #popularity should be fair criteria to determine which artist/band to choose
            response = requests.get(f"{SPOTIFY_API_URL}v1/search?q={selectedArtist}&type=artist",headers=getRequestHeader(self.__requestToken))
            if(response.status_code == 200):
                result = response.json()
                if result["artists"]["total"] == 0:
                    return(False,{"RESULT":"Artist not found"})
                else:
                    return (True,result)
            if response.status_code == 401 or response.status_code == 403:
                self.__getSpotifyToken()
                return self.__searchRandomArtistByGenre(genre)
            else:
                return (False,{"RESULT": "Server responds unexpectedly"})
            
        #Token check, if fails somehow reflesh it and recall the method to complete request. 
        #Might cause overflow, need to implement "depth limit" safeguard.(default depth limit around 1000)
        ##Enable 2 line below to limit it to 20
        #import sys
        #sys.setrecursionlimit(20)
        except TokenNull as error:##We can also create our own custom exception as well..
            self.getSpotifyToken()
            return self.__searchRandomArtistByGenre(genre)
        except Exception as error:
            print("Error on search artist. Error:",str(error))
            return (False,{"RESULT":"ERROR ON SEARCH ARTIST"})
    
    def __getArtistTopTracks(self,artistID):
            try:
                #Token check
                if self.__requestToken is None:
                    print("Search artist: Spotify token is null, creating one.")
                    self.__getSpotifyToken()
                
                #Get tracks belongs to choosen artist/band
                response = requests.get(f"{SPOTIFY_API_URL}v1/artists/{artistID}/top-tracks?market=TR",headers=getRequestHeader(self.__requestToken))
                if(response.status_code == 200):
                    result = response.json()
                    if len(result["tracks"]) == 0:
                        return (False,{f"RESULT":"No track found with given artist with ID:{artistID}."})
                    return (True,result)
                if response.status_code == 401 or response.status_code == 403:
                    self.__getSpotifyToken()
                    return self.__getArtistTopTracks(artistID)
                else:
                    return (False,{"RESULT": "Server responds unexpectedly"})
            
            except TokenNull as error:
                print(error)
                self.__getSpotifyToken()
                return self.__getArtistTopTracks(artistID)
            except Exception as error:
                print("Error on get artist top tracks. Error:",str(error))
                return (False,{"RESULT":"Error on getting artist's top tracks."})


    def getPlaylist(self,genre):

            #Search the randomly selected artist name based on genre.
            isArtistFound,artistList= spotifyService.__searchRandomArtistByGenre(genre)
            if not isArtistFound:
                return (False,{"RESULT":"NOT_FOUND_GENRE","MESSAGE":artistList["RESULT"]})
            
            #Sort found artists, search most popular ones top tracks. This filter/selection due to prevent false-positive results due to possible similar artist/band names
            isTracksFound,TrackList = self.__getArtistTopTracks(sortArtistsByPopularity(artistList)[0]["id"])
            if not isTracksFound:
                return (False,{"RESULT":"NOT_FOUND","MESSAGE":TrackList["RESULT"]})
            
            #Generate response data in desired format.
            return (True,{"RESULT":"SUCCESS","data":generateTopTracksResponse(TrackList)})
            
        

#Factory pattern like implementation might be better
#Yet avoding create token for each request to not to exceed request limit of api
spotifyService = SpotifyService()