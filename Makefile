.PHONY: clean runbe 
COV=.

help:
	@echo "clean - cleanup project"
	@echo "runbe - run backend app"


clean:
	rm -rf ./.pytest_cache
	rm -rf ./build
	rm -rf ./coverage
	find . -name \*.pyc -delete

runbe:
	src/manage.py runserver
