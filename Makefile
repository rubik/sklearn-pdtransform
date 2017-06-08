.PHONY: pep8 publish

pep8:
	pep8 pdtransform --ignore "E731"

publish:
	python setup.py sdist bdist_wheel upload
	python setup.py develop
