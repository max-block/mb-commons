VERSION = $(shell python3 setup.py --version | tr '+' '-')


clean:
	rm -rf .pytest_cache build dist *.egg-info


dist: clean
	python3 setup.py sdist bdist_wheel


upload: dist
	twine upload dist/*
	g at v$(VERSION)
