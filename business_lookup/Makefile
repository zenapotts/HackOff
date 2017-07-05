.PHONY: test checkstyle install
.PHONY: test-ci checkstyle-ci
.PHONY: server
.PHONY: wheel dist-wheel wheelhouse dist-wheelhouse tag rpm clean-env


ENV=./env
PYTHON=$(ENV)/bin/python
PIP=$(ENV)/bin/pip
NOSE=$(ENV)/bin/nosetests
FLAKE8=$(ENV)/bin/flake8
COVERAGE=$(ENV)/bin/coverage
GUNICORN=$(ENV)/bin/gunicorn
PACKAGEPATH=optimus.2ndsiteinc.com:/var/www/packages/python/releases/business_lookup
WORKSPACE:=$(shell pwd)
MAJOR_DISTRIBUTION:=6

ACTIVATE_ENV=source $(ENV)/bin/activate
DATE=$(shell date +'%Y-%m-%d_%H:%I:%S')
REMOTE=origin

PYPI_HOST=https://pi.builds.2ndsiteinc.com
PYPI_INDEX=$(PYPI_HOST)/dev/releases

ALL: help

TOP_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
MAKEFILE_INC_LOCATION := $(shell test -d $(TOP_DIR)../makefile.inc && echo $(TOP_DIR)../makefile.inc/.git || echo https://github.2ndsiteinc.com/dev/makefile.inc)

.PHONY: makefile.inc

makefile.inc:

makefile.inc/makefile.%: makefile.inc
	@$(MAKEFILE_UPDATE_SCRIPT) > /dev/null 2>&1

include makefile.inc/makefile.inc

env:
	test -d $(ENV) || virtualenv-2.7 $(ENV)

install: env ## Install dev dependencies
	$(PIP) install -i $(PYPI_INDEX) -r requirements-dev.txt
	$(PIP) install -e .

server: ## Run gunicorn
	$(GUNICORN) -c gunicorn.conf.py business_lookup.wsgi:app

test: install test-db # Run unit tests
	$(NOSE) $(NOSEOPTS) test

checkstyle: install ## Code lint tools
	$(FLAKE8) {business_lookup,test} || true

test-ci: install test-db ## Run tests for the CI environment
	$(COVERAGE) run -p --branch --source=business_lookup \
		$(NOSE) \
		--with-xunit \
		--xunit-file=xunit.xml
	$(COVERAGE) combine
	$(COVERAGE) xml

checkstyle-ci: install ## Run flake8 with CI output.
	$(FLAKE8) {business_lookup,test} > pep8.out || true

# Packaging targets/tasks
clean:
	rm -rf dist build wheelhouse

clean-env: ## Remove the virtualenv
	rm -rf $(ENV)

wheel: clean env guard-VERSION ## VERSION=x.y.z - Create a wheel
	git checkout release/$(VERSION)
	$(PIP) install wheel
	$(PYTHON) setup.py bdist_wheel

tag: guard-VERSION ## VERSION=x.y.z - Create a tag for the current checkout
	@if [ "$$(git rev-parse --abbrev-ref HEAD)" != "master" ]; then \
		echo "You must be on master to update the version"; \
		exit 1; \
	fi;
	echo $(VERSION) > ./business_lookup/VERSION
	git add ./business_lookup/VERSION
	git commit ./business_lookup/VERSION -m 'Bump version to $(VERSION)'
	git tag release/$(VERSION) -m 'business_lookup $(VERSION) - $(DATE)'
	git push $(REMOTE) --tags
	git push $(REMOTE) master

migrate: ## Run the DB migrations
	cd migrations/ && lb update

test-db: ## Create the test suite database
	./test/make_test_db.sh test_business_lookup business_lookup

rpm: guard-VERSION ## VERSION=x.y.z - Create an rpm for business_lookup
	@echo "Building RPM $(VERSION)"
	rm -rf $(WORKSPACE)'/rpm/'
	mkdir -p $(WORKSPACE)'/rpm/'{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	rpmbuild --define '_topdir $(WORKSPACE)/rpm' -ba business_lookup.spec \
		--define 'version $(VERSION)' \
		--define 'indexhost $(PYPI_INDEX)' \
		--define 'target_os el$(MAJOR_DISTRIBUTION)' \
		--define 'release $(BUILD_NUMBER).el$(MAJOR_DISTRIBUTION)'


.docker-image.t: Dockerfile requirements.txt requirements-dev.txt
	docker build --rm -t business_lookup.image -f Dockerfile .
	touch $@

