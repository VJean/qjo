def filter_events(events, artists):
    filtered = []
    for index, value in enumerate(artists):
        artists[index] = value.lower()
    for e in events:
        if any([artist in e.artist.lower() for artist in artists]):
            filtered.append(e)

    return filtered


def display_events(events):
    for e in events:
        print(e)
