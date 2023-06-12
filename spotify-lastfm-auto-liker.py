import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pylast

# Enter your Spotify API credentials here
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'

# Enter your Last.fm API credentials here
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
username = 'your_username'
password_hash = pylast.md5('your_password')

# Authenticate with the Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read"))

# Authenticate with the Last.fm API
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# Get the first batch of 50 saved tracks from Spotify
offset = 0
results = sp.current_user_saved_tracks(limit=50, offset=offset)

# Loop through the saved tracks and like each track on Last.fm
while results['items']:
    for item in results['items']:
        track = item['track']
        artist = track['artists'][0]['name']
        title = track['name']

        # Like the track on Last.fm
        network.get_track(artist, title).love()

        # Print a message to indicate that the track has been liked
        print(f"Liked '{title}' by {artist} on Last.fm.")

    # Check if there are more tracks to retrieve
    if results['next']:
        offset += 50
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
    else:
        break