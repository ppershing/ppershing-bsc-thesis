default: all

.PHONY: all
all: *
	cd image_compression; make
	cd signal_processing; make

.PHONY: clean
clean:
	cd image_compression; make clean
	cd signal_processing; make clean
