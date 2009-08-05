default: all

.PHONY:all
all: eps

CPARAM=-density 300

.PHONY: eps
eps: *.ppm *.dat
	for q in *.ppm ; do \
		w=`basename $$q .ppm`; \
		echo "convert $$q"; \
		convert $$w.ppm -density 140 -normalize $$w.eps;\
	done
	for q in *.tpl ; do\
		echo "run $$q";\
		gnuplot $$q; \
	done

.PHONY: clean
clean:
	-rm *.pyc
	-rm *.eps

.PHONY: full_clean
full_clean: clean
	-rm p*m*.ppm
