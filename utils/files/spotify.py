import spotipy,json
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '93dfe93f21fb46aaad10947eadfde562'
client_secret = '36bb6e205ff143c6aeab7c3eb9bafd3a'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def SearchFromSpotify(track_name,limit):
    results = sp.search(q=track_name, type='track', limit=limit)
    track_urls = [item["external_urls"]["spotify"] for item in results["tracks"]["items"]]
    return track_urls

