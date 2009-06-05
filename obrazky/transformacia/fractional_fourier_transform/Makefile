.PHONY: all
all: eps

data:
	python fractional.py

.PHONY: eps
eps:
	for q in *.tpl ; do echo $$q; ./$$q; done

