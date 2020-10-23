DIST := dist

build: clean
	python setup.py sdist
	python setup.py bdist_wheel --universal

clean:
	rm -rf $(DIST)

check: build
	twine check $(DIST)/*

upload: check
	twine upload $(DIST)/*
