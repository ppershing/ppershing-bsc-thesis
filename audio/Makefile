
default:all

SOX = /cygdrive/c/utility/sox/sox
source.raw: source.wav
	${SOX} source.wav -c 1  -r 22050 -f -8 source.raw

source2.raw: source2.wav
	${SOX} source2.wav -c 1  -r 22050 -f -8 source2.raw

tmp.wav: tmp.raw
	${SOX} -c 1  -r 22050 -f -8 tmp.raw tmp.wav

tmp.raw: source.raw test.py
	python test.py


.PHONY: all
all:
	cd mix_phase_magnitude; make
.PHONY: clean
clean:
	cd mix_phase_magnitude; make clean

.PHONY: full_clean
full_clean:
	cd mix_phase_magnitude; make full_clean
