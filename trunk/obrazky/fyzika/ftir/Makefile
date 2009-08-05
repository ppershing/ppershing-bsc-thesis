default: all

.PHONY: all
all: ftir_schema.eps

.PHONY: clean
clean:
	-rm *.eps

.PHONY: full_clean
full_clean: clean

ftir_schema.eps: ftir_schema.svg
	./svg2eps.sh ftir_schema

