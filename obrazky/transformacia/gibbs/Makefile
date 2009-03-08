
all:*.py *.dat *.tpl
	for q in *.py ; do echo $$q; ./$$q; done
	for q in *.tpl ; do echo $$q; ./$$q; done
	
.PHONY: clean
clean:
	-rm *.dat *.eps
