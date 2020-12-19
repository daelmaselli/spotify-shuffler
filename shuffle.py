import sys
import os
import spotipy
import spotipy.util as util
import random

limit = 100

scope = 'playlist-modify-public'

if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_uris = sys.argv[2:-1]
    dst_playlist_uri = sys.argv[-1]

else:
    print(f"Usage: {sys.argv[0]} username src_playlist_uri dst_playlist_uri")
    sys.exit()

try:
    token = util.prompt_for_user_token(username, scope)
except AttributeError:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)

    track_uris = []
    for playlist_uri in playlist_uris:

        playlist_uri_list = playlist_uri.split(':')

        user = playlist_uri_list[0]
        playlist_id = playlist_uri_list[2]
        offset = 0

        while True:
            items = sp.user_playlist_tracks(user=user, playlist_id=playlist_id, limit=limit, offset=offset)['items']
            for item in items:
                track_uris.append(item['track']['uri'])

            offset += limit

            if len(items) != limit:
                break

    random.shuffle(track_uris)

    dst_playlist_uri_list = dst_playlist_uri.split(':')
    dst_user = dst_playlist_uri_list[0]
    dst_playlist_id = dst_playlist_uri_list[2]

    sp.user_playlist_replace_tracks(username, dst_playlist_id, [])
    offset = 0
    while True:
        to_add = track_uris[offset:offset+limit]
        sp.user_playlist_add_tracks(username, dst_playlist_id, to_add)

        offset += limit

        if len(to_add) != limit:
            break

else:
    print(f"Couldn't get token for {username}")
