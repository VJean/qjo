# qjo - Qui joue où ?

## Run it yourself

```
# install with poetry
poetry install
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

## Tests

Run the tests with `make test`.

For convenience, a script is available to download the html page that's going to be parsed.
The tests suite mocks the classes so that they load the agenda from disk instead of making a http request.
To update the local files (for example if a website changed their layout), run `python3 -m tests.save`.
Be aware that by doing so you should also update the expectations in test cases.

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
* [x] cabaret sauvage
* [ ] alhambra
* [ ] salle pleyel
* [ ] new morning
* [ ] accor arena
* [ ] backstage by the mill
* [ ] la bellevilloise
