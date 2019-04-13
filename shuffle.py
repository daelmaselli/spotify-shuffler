import sys
import os
import spotipy
import spotipy.util as util
import random

limit = 100

scope = 'playlist-modify-public'

if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_uri = sys.argv[2]
else:
    print(f"Usage: {sys.argv[0]} username playlist_uri")
    sys.exit()

try:
    token = util.prompt_for_user_token(username, scope)
except AttributeError:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    playlist_uri_list = playlist_uri.split(':')

    user = playlist_uri_list[2]
    playlist_id = playlist_uri_list[4]

    playlist = sp.user_playlist(user, playlist_id, fields=['name', 'tracks'])

    playlist_name = f"{playlist['name']} - SHUFFLED"
    new_playlist = sp.user_playlist_create(username, playlist_name)

    track_uris = []
    offset = 0

    while True:
        items = sp.user_playlist_tracks(user=user, playlist_id=playlist_id, limit=limit, offset=offset)['items']
        for item in items:
            track_uris.append(item['track']['uri'])

        offset += limit

        if len(items) != limit:
            break

    random.shuffle(track_uris)
    offset = 0

    while True:
        to_add = track_uris[offset:offset+limit]
        sp.user_playlist_add_tracks(username, new_playlist['id'], to_add)

        offset += limit

        if len(to_add) != limit:
            break

else:
    print(f"Couldn't get token for {username}")
