.PHONY: init
init:
	pip install -U pre-commit
	pre-commit install

.PHONY: test
test:
	pre-commit run --all-files
