# qjo - Qui joue où ?

## Run it yourself

```
# set up a virtual env
python3 -m venv ./venv
source ./venv/bin/activate
# install deps
python -m pip install -r requirements.txt
# run tests
make test
# run main script
python -m qjo
# exit from virtualenv
deactivate
```

If you want to access a Spotify user's followed artists, you'll have to have a top-level `config.py` config file such as:
```
spotify_client_id='XXX'
spotify_client_secret='XXX'
spotify_redirect_uri='XXX'
```

You'll need a Spotify developer app set up to get those credentials.


## Naming

"Qui joue où ?" - "Who's touring where?" in French.

Also, i've-no-idea-how-to-name-my-project-so-let's-use-the-name-of-a-divinity :
* https://en.wikipedia.org/wiki/List_of_art_deities
* Euterpe : was the one of the Muses in Greek mythology, presiding over music

## Venues

* [x] maroquinerie
* [x] trianon
* [ ] cigale
* [ ] boule noire
* [ ] petit bain
* [ ] trabendo
* [ ] bataclan
* [ ] cabaret sauvage
* [ ] alhambra

## TODO
* Use a global `requests.Session` to avoid creating one for each venue parser
