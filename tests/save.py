from datetime import date

from qjo.venues import venues

# TODO check mtime different than today?

for venue in venues:
    venue_name = venue.__name__.lower()
    file_path = f"./tests/agendas/{venue_name}.html"
    try:
        with open(file_path, 'x') as f:
            print(f"Downloading {venue_name}'s agenda at {file_path}")
            f.write(str(venue._get_agenda_html()))
    except FileExistsError:
        print(f"Already downloaded {venue_name}'s agenda")
