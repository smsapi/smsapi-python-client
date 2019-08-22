.PHONY: dist tests

PROJECT := smsapi-client
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info


venv:
	virtualenv --python=python3 venv


install: venv
	. venv/bin/activate; pip install .


tests:
	. venv/bin/activate; python runtests.py


clean:
	rm -rf venv
	rm -rf dist build
	rm -rf $(EGG_INFO)

	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete


dist: clean
	. venv/bin/activate; setup.py sdist
	. venv/bin/activate; setup.py bdist_wheel


release: dist
	twine upload dist/*