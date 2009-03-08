.PHONY: all
all: tpl
	for q in *.tpl ; do echo $$q; ./$$q; done

.PHONY: tpl
tpl:
	for q in *.py ; do echo $$q; ./$$q; done

.PHONY: clean
clean:
	-rm *.dat *.eps
