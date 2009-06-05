default: all

.PHONY: all
all: *
	cd rady; make
	cd gibbs; make
	cd fractional_fourier_transform; make

.PHONY: clean
clean:
	cd gibbs; make clean
	cd rady; make clean
	cd fractional_fourier_transform; make clean

.PHONY: full_clean
full_clean: clean
	cd gibbs; make full_clean
	cd rady; make full_clean
	cd fractional_fourier_transform; make full_clean
