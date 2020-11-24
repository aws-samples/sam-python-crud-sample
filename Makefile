ifndef VERBOSE
MAKEFLAGS += --no-print-directory
endif
SHELL := /bin/bash
.DEFAULT_GOAL := help


help:
	@ echo "Use one of the following targets:"
	@ tail -n +8 Makefile |\
	egrep "^[a-z]+[\ :]" |\
	tr -d : |\
	tr " " "/" |\
	sed "s/^/ - /g"
	@ echo "Read the Makefile for further details"

venv virtualenv:
	@ echo "Creating a new virtualenv..."
	@ rm -rf env || true
	@ python3 -m venv env
	@ echo "Done, now you need to activate it. Run:"
	@ echo "source env/bin/activate"

activate:
	@ echo "Activating this Python3 Virtual Env:"
	@ bash --rcfile "./env/bin/activate"

requirements pip:
	@ if [ -z "${VIRTUAL_ENV}" ]; then \
		echo "Not inside a virtualenv."; \
		exit 1; \
	fi
	@ echo "Upgrading pip..."
	@ pip install --upgrade pip
	@ echo "Updating pip packages:"
	@ pip install -r "requirements.txt"
	@ echo "Self installing this package in edit mode:"
	@ pip install -e .
	@ echo "You are ready to go ;-)"

requirementsdev:
	@ if [ -z "${VIRTUAL_ENV}" ]; then \
		echo "Not inside a virtualenv."; \
		exit 1; \
	fi
	@ echo "Upgrading pip..."
	@ pip install --upgrade pip
	@ echo "Updating pip packages:"
	@ pip install -r "requirements_dev.txt"

cleanfull:
	@ echo "Cleaning old files..."
	@ rm -rf **/.pytest_cache
	@ rm -rf .tox
	@ rm -rf dist
	@ rm -rf build
	@ rm -rf **/__pycache__
	@ rm -rf *.egg-info
	@ rm -rf .coverage*
	@ rm -rf **/*.pyc
	@ rm -rf env
	@ rm -rf local
	@ rm -rf .aws-sam
	@ echo "All done!"

clean:
	@ echo "Cleaning old files..."
	@ rm -rf **/.pytest_cache
	@ rm -rf .tox
	@ rm -rf dist
	@ rm -rf build
	@ rm -rf **/__pycache__
	@ rm -rf *.egg-info
	@ rm -rf .coverage*
	@ rm -rf **/*.pyc
	@ echo "All done!"

dockerrun dkr:
	@ docker run -p 8000:8000 -d --rm --network lambda-local --name dynamodb -v $(CURDIR)/local/dynamodb:/data/ amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath /data

dockerstop dks:
	@ docker stop dynamodb

containerprune ctp:
	@ docker container prune

dockernetwork dkn:
	@ docker network create lambda-local

server:
	@ sam local start-api --docker-network lambda-local --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL

test:
	@ tox

package:
	@ python setup.py sdist
	@ echo "Your package is in the dist directory."

upload pypi:
	@ python setup.py sdist upload
