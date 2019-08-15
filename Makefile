.PHONY: help clean docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "  docs	create pydocs for all relveant modules"
	@echo "	 test	run all tests with coverage"

clean:
	rm -rf dist/*

docs:
	$(MAKE) -C docs html

package:
	python setup.py sdist
	python setup.py bdist_wheel

test:
	coverage run -m unittest discover
	coverage html
