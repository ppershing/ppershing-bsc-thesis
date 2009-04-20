default: all
.PHONY: all
all: interferencia_1.eps interferencia_2.eps

interferencia_1.eps: interferencia_1.svg
	./svg2eps.sh interferencia_1

interferencia_2.eps: interferencia_2.svg
	./svg2eps.sh interferencia_2

.PHONY: clean
clean:
	-rm *.eps

.PHONY: full_clean
full_clean: clean
