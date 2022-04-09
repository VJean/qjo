PHONY: test

test:
	@if ! test -d ./tests/agendas; then\
		echo "First, let's save the agendas locally";\
		mkdir ./tests/agendas/;\
		python3 -m tests.save;\
	fi
	@echo To update the tests datasets, run: python3 -m tests.save
	@echo Running the tests
	python3 -m unittest tests/test_qjo.py
