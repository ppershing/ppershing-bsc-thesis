.PHONY: all
all: gibbs_figura.eps dat
	for q in *.tpl ; do echo $$q; ./$$q; done

gibbs_figura.eps: gibbs_figura.png
	convert $? -density 150 $@


.PHONY: dat
dat: lin_10.dat sincintegral.dat

lin_10.dat: gibbs.py
	python gibbs.py

sincintegral.dat: sincintegral.py
	python sincintegral.py

.PHONY: clean
clean:
	-rm *.eps

.PHONY: full_clean
full_clean: clean
	-rm *.dat
