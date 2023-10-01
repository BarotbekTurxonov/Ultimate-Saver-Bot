import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '93dfe93f21fb46aaad10947eadfde562'
client_secret = '36bb6e205ff143c6aeab7c3eb9bafd3a'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for a track
track_name = 'jaloliddin Ahmadaliyev'
results = sp.search(q=track_name, type='track', limit=5)

# Extract information about the first track in the search results
if len(results['tracks']['items']) > 0:
    track = results['tracks']['items'][0]
    print(f"Track Name: {track['name']}")
    print(f"Artist: {track['artists'][0]['name']}")
    print(f"Album: {track['album']['name']}")
    print(f"Spotify URI: {track}")
else:
    print("No results found for the track name.")

