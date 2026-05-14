.PHONY: dist tests build-deps release-deps

PYTHON = python3

PROJECT := smsapi-client
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info


venv:
	@${PYTHON} --version || (echo "Python is not installed."; exit 1)
	${PYTHON} -m venv venv


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


build-deps: venv
	. venv/bin/activate; pip install --upgrade setuptools wheel


release-deps: venv
	. venv/bin/activate; pip install --upgrade twine


dist: clean build-deps
	. venv/bin/activate; python setup.py sdist
	. venv/bin/activate; python setup.py bdist_wheel


release: dist release-deps
	. venv/bin/activate; python -m twine upload dist/*