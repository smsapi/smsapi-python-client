.PHONY: dist tests

PYTHON = python

PROJECT := smsapi-client
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info


venv:
	@${PYTHON} --version || (echo "Python is not installed."; exit 1)
	virtualenv --python=${PYTHON} venv


install: venv
	. venv/bin/activate; pip install .


tests:
	. venv/bin/activate; python runtests.py


clean-venv:
	rm -rf venv


clean:
	rm -rf dist build
	rm -rf $(EGG_INFO)

	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete


clean-all: clean clean-venv


dist: clean
	. venv/bin/activate; python setup.py sdist
	. venv/bin/activate; python setup.py bdist_wheel


release: dist
	python -m twine upload dist/*