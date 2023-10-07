PHONY: test

test:
	@if ! test -d ./tests/agendas; then\
		echo "First, let's save the agendas locally";\
		mkdir ./tests/agendas/;\
		poetry run python3 -m tests.save;\
	fi
	@echo To update the tests datasets, run: poetry run python3 -m tests.save
	@echo Running the tests
	poetry run python3 -m unittest tests/test_qjo.py
