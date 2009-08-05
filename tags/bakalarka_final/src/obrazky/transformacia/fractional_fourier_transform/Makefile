.PHONY: all
all: eps

data:	rect_000.dat

rect_000.dat:
	python fractional.py

.PHONY: eps
eps:
	for q in *.tpl ; do echo $$q; ./$$q; done

.PHONY: clean
clean:
	-rm *.eps

.PHONY: full_clean
full_clean: clean
	-rm *.dat *.eps
