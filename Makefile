DIST := dist

all: clean
	python setup.py sdist
	python setup.py bdist_wheel --universal

clean:
	rm -rf $(DIST)

check:
	twine check $(DIST)/*

upload:
	twine upload $(DIST)/*
