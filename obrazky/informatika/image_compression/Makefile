.PHONY: all

all: ppm combined_histogram.eps zig_zag.eps
	convert -density 200 image.ppm -colorspace Gray image.eps
	convert -density 200 -sigmoidal-contrast 7,10\% dct.ppm dct.eps
	convert -density 200 -sigmoidal-contrast 7,10\% dft.ppm dft.eps
	convert -density 200 dct_histogram.ppm  dct_histogram.eps
	convert -density 200 dft_histogram.ppm dft_histogram.eps

zig_zag.eps: zig_zag.svg
	./svg2eps.sh zig_zag

.PHONY: ppm
ppm: dct_histogram.ppm dft_histogram.ppm dct.ppm dft.ppm

dct_histogram.ppm dct.ppm \
dft_histogram.ppm dft.ppm: image.ppm dct_dft_energy.py
	python dct_dft_energy.py

combined_histogram.eps: *.ppm
	convert -channel blue -fx "1" \
		-channel green -fx "1" \
		dct_histogram.ppm dct_histogram.bmp
	convert -channel red -fx "1" \
		-channel blue -fx "1"\
		dft_histogram.ppm dft_histogram.bmp
	composite -compose multiply \
		dct_histogram.bmp dft_histogram.bmp \
		combined_histogram.ppm
	convert -density 200 \
		combined_histogram.ppm -colorspace Gray \
		-gamma 0.5 combined_histogram.eps
	rm dct_histogram.bmp
	rm dft_histogram.bmp
	rm combined_histogram.ppm
	
.PHONY: clean
clean:
	-rm *.eps
	-rm *.pyc

.PHONY: full_clean
full_clean: clean
	-rm dct*.ppm
	-rm dft*.ppm
