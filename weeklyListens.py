import base64
import json
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy.util as util
from json.decoder import JSONDecodeError
from dotenv import load_dotenv
from datetime import timedelta, datetime

from recommendations import *

from topfifty import *
from createPlaylist import *

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
client_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# USERID 31aewxqbr5kesprsnjfteqv6rqb4
SPOTIFY_API_URL = 'https://api.spotify.com/v1'
CREATE_PLAYLIST_ENDPOINT = '/users/imokayj/playlists'

scope = "playlist-modify-private playlist-modify-public user-read-recently-played user-read-private user-top-read"

username = "31aewxqbr5kesprsnjfteqv6rqb4"

try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spobj = spotipy.Spotify(auth=token)

    
    

def main():
    # gets the recent songs
    recents = get_recent_fifty(spobj)
    
    #gets the genes of the songs and then filters based off the api
    genres =  get_genres(spobj, recents)
    genres = check_genres(spobj, genres)

    # split the generes into multiple lists since the api has a maximum call of 5
    split_genres = split_into_subsets(genres)
    limit = int(50 / len(split_genres))
    newList = []
    for gen in split_genres:
        print(gen)
        newList += recommend(spobj, gen, limit = limit) 

    # creates playlist
    playlist_name = 'My API Playlist'
    playlist_description = 'i made this playlist in VScode'

    create_playlist(spobj, playlist_name, playlist_description)

    # creates the list of track ids and adds them to said playlist
    list_of_uris = get_track_uri(spobj, newList)
    playlist_id = get_playlist_id(spobj, playlist_name)

    add_to_playlist(spobj, playlist_id, list_of_uris)


main()


