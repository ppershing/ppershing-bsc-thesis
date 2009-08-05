default: all

.PHONY:all
all: phase_magnitude

CPARAM=-density 320 -normalize

.PHONY: phase_magnitude
phase_magnitude: p1m1.eps p1m2.eps p1mc.eps \
		 p2m1.eps p2m2.eps p2mc.eps \
		 pcm1.eps pcm2.eps

p1m1.eps: p1m1.ppm
	convert ${CPARAM} $? $@

p1m2.eps: p1m2.ppm
	convert ${CPARAM} $? $@

p1mc.eps: p1mc.ppm
	convert ${CPARAM} $? $@

p2m1.eps: p2m1.ppm
	convert ${CPARAM} $? $@

p2m2.eps: p2m2.ppm
	convert ${CPARAM} $? $@

p2mc.eps: p2mc.ppm
	convert ${CPARAM} $? $@

pcm1.eps: pcm1.ppm
	convert ${CPARAM} $? $@

pcm2.eps: pcm2.ppm
	convert ${CPARAM} $? $@

p1m1.ppm p1m2.ppm p1mc.ppm \
p2m1.ppm p2m2.ppm p2mc.ppm \
pcm1.ppm pcm2.ppm: source1.ppm source2.ppm mix_phase_magnitude.py
	python mix_phase_magnitude.py

.PHONY: clean
clean:
	-rm *.pyc
	-rm *.eps

.PHONY: full_clean
full_clean: clean
	-rm p*m*.ppm
