.PHONY: dist tests

PYTHON := python3

PROJECT := smsapi-client
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info


venv:
	virtualenv --python=python3 venv


install: venv
	. venv/bin/activate; pip install .


tests:
	$(PYTHON) runtests.py


clean:
	rm -rf venv
	rm -rf dist build
	rm -rf $(EGG_INFO)

	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete


dist: clean
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel


release: dist
	twine upload dist/*