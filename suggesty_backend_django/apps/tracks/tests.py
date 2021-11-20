import json,os
import pathlib
from django.http import response
from django.test import TestCase, client
from django.test import Client

from spotifyservice.spotifyservice import SpotifyService

class TrackTestCase(TestCase):
    genreData = {}
    def setUp(self):
        self.client = Client()
    
    def test_load_genre_data(self):
        print("Testing: Genre data load from file")
        try:
            path = pathlib.Path(__file__).parent.resolve().parent.parent
            genreData = json.load(open(os.path.join(path,"spotifyservice","genres.json",),mode='r' ,encoding = "utf8"))   
            self.assertNotEqual(len(genreData),0)
            self.genreData = genreData
        except:
            self.fail("Genre JSON loading attempt throw an exception")

    def test_spotify_auth(self):
        spotifyClient = SpotifyService()
        result = spotifyClient.testSpotifyToken()
        print("Testing: Spotify API Key and Autharization")
        self.assertEqual(result.status_code,200)


    def test_route_invalid_methods(self):
        print("Testing: Route with invalid methods")
        response = self.client.post('/v1/tracks/')
        self.assertEqual(response.status_code,404)
        response = self.client.delete('/v1/tracks/')
        self.assertEqual(response.status_code,404)
        response = self.client.put('/v1/tracks/')
        self.assertEqual(response.status_code,404)
        response = self.client.patch('/v1/tracks/')
        self.assertEqual(response.status_code,404)

    def test_route_empty(self):
        response = self.client.get('/v1/tracks/')
        print("Testing: Request without parameter")
        self.assertEqual(response.status_code,404)
    
    def test_route_name_like_parameter(self):
        response = self.client.get('v1/tracks')
        print("Testing: Route like parameter")
        self.assertEqual(response.status_code,404)     

    #This one also validates request responses inherently due to checks in endpoint and checks in call chain     def test_route_valid_paramaters(self):
        try:
            path = pathlib.Path(__file__).parent.resolve().parent.parent
            genreData = json.load(open(os.path.join(path,"spotifyservice","genres.json",),mode='r' ,encoding = "utf8"))   
            self.assertNotEqual(len(genreData),0)
            self.genreData = genreData
        except:
            self.fail("Genre JSON loading attempt throw an exception")
 
        print("Testing: Valid parameters total of "+str(len(self.genreData)))
        for genre in self.genreData:
            print("Test genre:",genre)
            response =self.client.get('/v1/tracks/'+genre)
            self.assertEqual(response.status_code,200)

        
    
