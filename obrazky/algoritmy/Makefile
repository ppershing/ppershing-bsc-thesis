default: all

.PHONY: all
all: butterfly_dif.eps butterfly_dit.eps dif.eps dit.eps

.PHONY: clean
clean:
	-rm *.eps

.PHONY: full_clean
full_clean: clean

butterfly_dif.eps: butterfly_dif.svg
	./svg2eps.sh butterfly_dif

butterfly_dit.eps: butterfly_dit.svg
	./svg2eps.sh butterfly_dit

dif.eps: dif.svg
	./svg2eps.sh dif

dit.eps: dit.svg
	./svg2eps.sh dit
