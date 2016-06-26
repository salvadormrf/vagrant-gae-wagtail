all: deps

################################################################################
# Cleanup tasks ################################################################
################################################################################

clean-pyc:
	@ echo 'Deleting all pyc files'
	@ find . -type f -name "*.py[c|o]" -delete
	@ find . -type d -name "__pycache__" -delete
	@ find . -name '*~' -delete

clean: clean-pyc
	@ rm -rf db.sqlite3
	@ rm -rf vendor
	@ rm -rf static
	@ echo "Cleaned"

################################################################################
# Other tasks ##################################################################
################################################################################

lint:
	flake8 ./project* --ignore=F403,E501,E128,E124,N806

################################################################################
# Build tasks ##################################################################
################################################################################

build-deps:
	@ pip install -r requirements-build.txt

deps:
	@ cmp -s requirements.txt vendor/requirements.txt; \
  	RETVAL=$$?; \
  	if [ $$RETVAL -eq 0 ]; then \
		echo "Dependencies up-to-date"; \
  	else \
		echo "Dependencies need updating"; \
		rm -rf vendor/; \
		pip install -t vendor -r requirements.txt && cp requirements.txt vendor/; \
		rm -rf vendor/PIL; \
  	fi

build: deps build-deps static

################################################################################
# Database tasks ###############################################################
################################################################################

migrate:
	@ echo "Migrating tables"
	@ python manage.py migrate --noinput

################################################################################
# Development tasks ############################################################
################################################################################

run_cmd:
	gcloud preview app run app.yaml \
		--host 0.0.0.0 \
		--admin-host 0.0.0.0 \
		--storage-path=~/appengine_storage \
		--blobstore-path=~/appengine_blobstore \
		--datastore-path=~/appengine_datastore \
		--verbosity info

kill_server:
	@ lsof -P | grep ':8080' | awk '{print $2}' | xargs kill -9

run: deps build-deps migrate kill_server run_cmd

run_fast: deps build-deps kill_server run_cmd


.PHONY: deps build-deps build lint run run_fast