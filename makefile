TEX = xelatex
OPR = $(shell uname -s)

ifeq ($(OPR), Darwin)
	DOC = open -a Preview
else
	DOC = zathura
endif

build:
	python3 -m pkgs.core

clean:
	find . -type f -name main.aux    | xargs rm -rf
	find . -type f -name main.log    | xargs rm -rf
	find . -type f -name main.pdf    | xargs rm -rf
	find . -type d -name __pycache__ | xargs rm -rf

ready:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -U pip; \
	pip install -r requirements.txt; \
	deactivate

.PHONY: build clean ready
