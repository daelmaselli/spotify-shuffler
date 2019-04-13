# Spotify playlist shuffler

## What is it?
The Spotify playlist shuffler is a small command line tool that, as the name implies, shuffles 
a playlists and adds it's to the current user's Spotify library.

## Usage
First, you have to set the needed environment variables.

### Windows 
```
set SPOTIPY_CLIENT_ID='client_id'
set SPOTIPY_CLIENT_SECRET='client_secret'
set SPOTIPY_REDIRECT_URI='redirect_uri'
```

### Mac & Linux 
```
export SPOTIPY_CLIENT_ID='client_id'
export SPOTIPY_CLIENT_SECRET='client_secret'
export SPOTIPY_REDIRECT_URI='redirect_uri'
```

*client_id*, *client_secret* can be found here: https://developer.spotify.com/dashboard/applications.

*redirect_uri* has to be set at this link aswell.
It doesn't really matter what URI you choose, as it doesn't get used in this app.

