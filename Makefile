VERSION := 0.1.0

start:
	python main.py

tag:
	git tag -m "v${VERSION}" v${VERSION}
	git push --tags
