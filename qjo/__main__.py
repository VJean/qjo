#!/usr/bin/env python3

import logging
import config
from qjo import filter_events, display_events
from qjo.venues import venues
from multiprocessing import Pool

logging.basicConfig(format='[%(asctime)s][%(name)s][%(process)d][%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

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

    logger.info(f"Retrieving {results['artists']['total']} followed artists")

    while results["artists"]["next"]:
        artists.extend([a["name"] for a in results["artists"]["items"]])
        results = sp.next(results["artists"])

    del sp
    return artists


with Pool() as pool:
    logger.info("Gathering concerts...")
    async_results = [pool.apply_async(venue.get_events, ()) for venue in venues]
    events = []
    for result in async_results:
        events.extend(result.get())
    logger.info(f"Found {len(events)} events")
    logger.info("Sorting by date...")
    events.sort()
    logger.info("Filtering with followed artists...")
    events = filter_events(events, get_followed_artists())
    display_events(events)
