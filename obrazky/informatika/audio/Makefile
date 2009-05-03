default: all

.PHONY: all

all: *.tpl data lapped_transform.eps post_windowing.eps
	for q in *.tpl ; do echo $$q; ./$$q; done

lapped_transform.eps: lapped_transform.svg
	./svg2eps.sh lapped_transform

post_windowing.eps: post_windowing.svg
	./svg2eps.sh post_windowing

.PHONY: data
data: dct.dat mdct.dat

dct.dat mdct.dat: sample.dat
	python dct_vs_mdct.py

.PHONY: clean
	-rm *.pyc
	-rm dct.dat mdct.dat
	-rm *.eps
.PHONY: full_clean
full_clean: clean
