
SOX = /cygdrive/c/utility/sox/sox
source.raw: source.wav
	${SOX} source.wav -c 1  -r 22050 -f -8 source.raw


tmp.wav: tmp.raw
	${SOX} -c 1  -r 22050 -f -8 tmp.raw tmp.wav

tmp.raw: source.raw test.py
	python test.py
