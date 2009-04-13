.PHONY:all

all: correlation.eps pattern.eps source.eps


correlation_gray.ppm: pattern.ppm source.ppm
	python correlate.py

correlation.eps: correlation_gray.ppm
	convert correlation_gray.ppm -density 300 correlation.eps

pattern.eps:
	convert pattern.ppm -density 300 pattern.eps

source.eps:
	convert source.ppm -density 300 source.eps
