TEX_ENGINE = xelatex
OPR_SYSTEM = $(shell uname -s)

ifeq ($(OPR_SYSTEM), Darwin)
	DOC_VIEWER = open -a Preview
else
	DOC_VIEWER = zathura
endif

build:
	python3 -m pkgs.core

black:
	isort pkgs/core.py
	black -l 79 pkgs/core.py

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

.PHONY: build black clean ready
