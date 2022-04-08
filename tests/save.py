import os, sys
from datetime import date
from qjo.venues import venues

folder_path = "./tests/agendas/"

# test folder existence
if not os.path.isdir(folder_path):
    print("Missing test files folder, please run 'make test'")
    sys.exit(1)

for venue in venues:
    venue_name = venue.__name__.lower()
    file_path = f"./tests/agendas/{venue_name}.html"

    # TODO check mtime different than today?
    with open(file_path, "w") as f:
        print(f"Downloading {venue_name}'s agenda at {file_path}")
        f.write(str(venue._get_agenda_html()))
