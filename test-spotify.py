import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.spotify_client_id,
                                               client_secret=config.spotify_client_secret,
                                               redirect_uri=config.spotify_redirect_uri,
                                               scope="user-follow-read"))

results = sp.current_user_followed_artists()
artists = []

print(f"Following {results['artists']['total']} artists")

while results['artists']['next']:
    artists.extend([a['name'] for a in results['artists']['items']])
    results = sp.next(results['artists'])

for idx, item in enumerate(artists):
    print(idx, item)

