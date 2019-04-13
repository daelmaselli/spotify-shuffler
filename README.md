# Spotify playlist shuffler

## What is it?
The Spotify playlist shuffler is a small command line tool that, as the name implies, shuffles 
a playlists and adds it to the current user's Spotify library.

## Usage
Create a new Spotify application on the following link: https://developer.spotify.com/dashboard/applications.
Thereafter, open up the command line and be sure to be located in the root directory of this project.

### Setup
Create a new file called `spotipy.ini` and give it the following content.

```
SPOTIPY_CLIENT_ID=client_id
SPOTIPY_CLIENT_SECRET=client_secret
SPOTIPY_REDIRECT_URI=redirect_uri
```

*client_id* and *client_secret* can be found on the Spotify page of your application.

*redirect_uri* has to be accord with redirect URI you set at this same page.
It doesn't really matter what URI you choose.  
*For example: https://www.spotify.com.*

### Run

```python shuffle.py 'your_spotify_user_id' 'spotify_playlist_uri'```
