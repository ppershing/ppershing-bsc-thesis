.PHONY: all

INKSCAPE=/cygdrive/c/Program\ Files/Inkscape/inkscape.exe

all: *.ppm combined_histogram.eps zig_zag.eps
	convert -density 200 image.ppm image.eps
	convert -density 200 dct.ppm dct.eps
	convert -density 200 dft.ppm dft.eps
	convert -density 200 dct_histogram.ppm  dct_histogram.eps
	convert -density 200 dft_histogram.ppm dft_histogram.eps

zig_zag.eps: zig_zag.svg
	CYG_WD=`pwd`; DOS_WD=`cygpath -d $$CYG_WD`; \
	echo "working directory for inkscape $$DOS_WD"; \
	${INKSCAPE} $$DOS_WD/zig_zag.svg --export-eps=$$DOS_WD/zig_zag.eps

combined_histogram.eps: *.ppm
	convert -channel blue -fx "1" \
		-channel green -fx "1" \
		dct_histogram.ppm dct_histogram.bmp
	convert -channel red -fx "1" \
		-channel green -fx "1"\
		dft_histogram.ppm dft_histogram.bmp
	composite -compose multiply \
		dct_histogram.bmp dft_histogram.bmp \
		combined_histogram.ppm
	convert -density 200 \
		combined_histogram.ppm combined_histogram.eps
	rm dct_histogram.bmp
	rm dft_histogram.bmp
	rm combined_histogram.ppm
	
.PHONY: clean
clean:
	-rm *.eps
