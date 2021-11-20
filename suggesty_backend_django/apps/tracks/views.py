from json.decoder import JSONDecodeError
from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponseServerError
from django.http import JsonResponse
import logging

from spotifyservice.spotifyservice import spotifyService

# Get an instance of a logger
logger = logging.getLogger(__name__)

###
# Endpoint to request list of tracks of random artist/group from static list with given genre.
# Method(s) : Get | Parameters : genre:string
###
async def tracks(request,genre):
    if request.method == "GET":
        try:
            isSuccess,playlistResponse = spotifyService.getPlaylist(genre.lower())
            if isSuccess:
                return JsonResponse(playlistResponse,status =200)
            else:
                if(playlistResponse["RESULT"] == "NOT_FOUND"):
                    return JsonResponse(playlistResponse,status =404)
                if(playlistResponse["RESULT"] == "NOT_FOUND_GENRE"):
                    return JsonResponse(playlistResponse,status =400)
        except Exception as error:
            #add logging
            print("Error on tracks: " + str(error))
            return JsonResponse({"RESULT":"ERROR","MESSAGE":"Server-side exception."},status=500)
    else:
        return JsonResponse({"RESULT":"NOT_FOUND","MESSAGE":"Invalid method. Route does not support this method.."},status=404)

