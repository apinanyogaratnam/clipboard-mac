start:
	python main.py

tag:
	git tag -m "v${VERSION}" v${VERSION}
	git push --tags
