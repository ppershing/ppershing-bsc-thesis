default: all

.PHONY: all
all: *.tpl
	for q in *.tpl ; do echo $$q; ./$$q; done
	
.PHONY: clean
clean:
	-rm *.eps

.PHONY: full_clean
full_clean: clean
