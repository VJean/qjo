#!/usr/bin/env python3

import config
from qjo.venues import venues
from multiprocessing import Pool


def get_followed_artists():
    # TODO: add ability to either:
    # not load any followed artist
    # load from file
    # load from spotify
    # load from deezer
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=config.spotify_client_id,
            client_secret=config.spotify_client_secret,
            redirect_uri=config.spotify_redirect_uri,
            scope="user-follow-read",
        )
    )

    results = sp.current_user_followed_artists()
    artists = []

    print(f"Retrieving {results['artists']['total']} followed artists")

    while results["artists"]["next"]:
        artists.extend([a["name"] for a in results["artists"]["items"]])
        results = sp.next(results["artists"])

    del sp
    return artists


with Pool() as pool:
    async_results = [pool.apply_async(venue.get_events, ()) for venue in venues]
    events = []
    for result in async_results:
        events.extend(result.get())
    events.sort()
    print(events)
