default: all

.PHONY: all

all: *.tpl data lapped_transform.eps post_windowing.eps\
	obrazky_k_textu
	for q in *.tpl ; do echo $$q; ./$$q; done

.PHONY: obrazky_k_textu
obrazky_k_textu: equi_loudness.eps temporal_masking.eps \
	simultaneous_masking.eps mp3_flow_diagram.eps

equi_loudness.eps: equi_loudness.gif
	convert $< -density 175 $@

temporal_masking.eps: temporal_masking.gif
	convert $< -density 175 $@

simultaneous_masking.eps: simultaneous_masking.gif
	convert $< -density 175 $@

mp3_flow_diagram.eps: mp3_flow_diagram.png
	convert $< -density 150 $@

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
