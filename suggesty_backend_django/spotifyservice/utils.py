import json,random,os

from common.Exceptions import TokenNull

try:
    #Since we are working with files, instead of reading it every single time, load it once.
    genreData = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'genres.json'),mode='r' ,encoding = "utf8"))   
    print("Genre data loaded.")
except:
    print("Genre data load failed. Service aborts")
    exit()

def getRequestHeader(token):
        if token is None:
            raise TokenNull("Request Token is not set")
        return {"Authorization" : f'{token["token_type"]} {token["access_token"]}'}


def getRandomArtistByGenre(genre):  
    if genre in genreData:
        return (True,random.choice(genreData[genre]))
    else:
        return(False,None)

def sortArtistsByPopularity(tracks):#Just to be sure we always want to pick the most popular artist/band so sort them and pick the best
    return sorted(tracks["artists"]["items"],key = lambda item:item["popularity"],reverse=True)

def generateTopTracksResponse(trackList):
    responseData = []
    for track in trackList["tracks"]:
        data = {
            "artist": track["artists"][0]["name"],
            "track":track["name"],
            "album_image_url":track["album"]["images"][1]["url"],
            "preview_url":track["preview_url"]
        }
        responseData.append(data)
    return responseData[:10]#Just in case, since limitation asked to be 10
