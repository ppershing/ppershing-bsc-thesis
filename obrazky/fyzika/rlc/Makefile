default: all

.PHONY: all
all: tpl rc_obvod.eps
	for q in *.tpl ; do echo $$q; ./$$q; done

rc_obvod.eps: rc_obvod.svg
	./svg2eps.sh rc_obvod

.PHONY: tpl
tpl:
	for q in *.py ; do echo $$q; ./$$q; done

.PHONY: clean
clean:
	-rm rc_priebeh*.dat *.eps
	-rm *.pyc

.PHONY: full_clean
full_clean: clean
