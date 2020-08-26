DIST := dist

all:
	rm -rf $(DIST)
	python setup.py sdist
	python setup.py bdist_wheel --universal

check:
	twine check $(DIST)/*
