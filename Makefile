.PHONY: clean pep8 tests

CWD="`pwd`"
PROJECT_NAME = python-simple-swiftclient
PROJECT_HOME ?= $(CWD)

clean:
	@echo "Cleaning up *.pyc files"
	@find . -name "*.pyc" -delete
	@find . -name "*.~" -delete
	rm -rf build/ dist/ python_simple_swiftclient.egg-info

build:
	@echo "Building Python simple swiftclient."
	python ./setup.py build

install:
	@echo "Install Python simple swiftclient."
	python ./setup.py install
