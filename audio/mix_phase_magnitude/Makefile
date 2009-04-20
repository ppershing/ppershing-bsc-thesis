.PHONY: all
all: phase_magnitude

SOX = /cygdrive/c/utility/sox/sox
source.raw: source.wav
	${SOX} source.wav -c 1  -r 22050 -f -8 source.raw

source2.raw: source2.wav
	${SOX} source2.wav -c 1  -r 22050 -f -8 source2.raw


p1m1.raw p1m2.raw p1mc.raw \
p2m1.raw p2m2.raw p2mc.raw \
pcm1.raw pcm2.raw: source.raw source2.raw mix_phase_magnitude.py
	python mix_phase_magnitude.py

p1m1.wav: p1m1.raw
	${SOX} -c 1  -r 22050 -f -8 p1m1.raw p1m1.wav
p1m2.wav: p1m2.raw
	${SOX} -c 1  -r 22050 -f -8 p1m2.raw p1m2.wav
p2m1.wav: p2m1.raw
	${SOX} -c 1  -r 22050 -f -8 p2m1.raw p2m1.wav
p2m2.wav: p2m2.raw
	${SOX} -c 1  -r 22050 -f -8 p2m2.raw p2m2.wav
p1mc.wav: p1mc.raw
	${SOX} -c 1  -r 22050 -f -8 p1mc.raw p1mc.wav
pcm1.wav: pcm1.raw
	${SOX} -c 1  -r 22050 -f -8 pcm1.raw pcm1.wav
p2mc.wav: p2mc.raw
	${SOX} -c 1  -r 22050 -f -8 p2mc.raw p2mc.wav
pcm2.wav: pcm2.raw
	${SOX} -c 1  -r 22050 -f -8 pcm2.raw pcm2.wav

.PHONY: phase_magnitude
phase_magnitude: p1m1.wav p1m2.wav p2m1.wav p2m2.wav \
		p1mc.wav pcm1.wav p2mc.wav pcm2.wav

.PHONY: clean
clean:
	-rm *.pyc
	-rm p*m*.wav

.PHONY: full_clean
full_clean: clean
	-rm  *.raw
