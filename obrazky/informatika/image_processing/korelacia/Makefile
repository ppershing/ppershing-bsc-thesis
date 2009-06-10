.PHONY:all

all: correlation.eps pattern.eps source.eps


correlation.eps: correlation_gray.ppm
	convert correlation_gray.ppm -density 300 -gamma 1.5 correlation.eps

pattern.eps:
	convert pattern.ppm -density 300 pattern.eps

source.eps:
	convert source.ppm -density 300 source.eps

.PHONY: clean
clean:
	-rm *.pyc
	-rm *.eps

.PHONY: full_clean
full_clean: clean
	-rm correlation*.ppm

correlation_color.ppm correlation_gray.ppm: \
		pattern.ppm source.ppm correlate.py
	python correlate.py
