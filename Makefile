.PHONY: dist tests

PYTHON := python3

PROJECT := smsapi-client
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info


tests:
	$(PYTHON) runtests.py


clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf dist build
	rm -rf $(EGG_INFO)


dist: clean
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel


upload:
	twine upload dist/*