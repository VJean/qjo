import os, sys
from datetime import date
from qjo.venues import venues

folder_path = "./tests/agendas/"

# TODO add flags to update only one venue or a set of venues or all venues

# test folder existence
if not os.path.isdir(folder_path):
    print("Missing test files folder, please run 'make test'")
    sys.exit(1)

for venue in venues:
    venue_name = venue.__name__.lower()
    file_path = os.path.join(folder_path, f"{venue_name}.html")

    with open(file_path, "w") as f:
        print(f"Downloading {venue_name}'s agenda at {file_path}")
        f.write(str(venue._get_agenda_html()))
