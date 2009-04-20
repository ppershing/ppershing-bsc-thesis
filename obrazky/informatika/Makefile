default: all

.PHONY: all
all: *
	cd image_compression; make
	cd signal_processing; make
	cd image_processing; make
	cd audio; make

.PHONY: clean
clean:
	cd image_compression; make clean
	cd signal_processing; make clean
	cd image_processing; make clean
	cd audio; make clean

.PHONY: full_clean
full_clean: clean
	cd image_compression; make full_clean
	cd signal_processing; make full_clean
	cd image_processing; make full_clean
	cd audio; make full_clean
