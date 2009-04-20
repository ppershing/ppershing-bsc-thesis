default: pdf

fast:
	cslatex main
	
main.dvi: *.tex *.bib Makefile */*.tex code/* obrazky tabulky
	rm -f *.toc
	cslatex main
	bibtex main
	cslatex main
	cslatex main

main.ps: main.dvi
	dvips main.dvi

dvi: main.dvi

ps: main.ps

#main.pdf: *.tex *.bib Makefile
#	rm -f *.toc
#	pdfcslatex main
#	bibtex main
#	pdfcslatex main
#	pdfcslatex main
main.pdf: Makefile main.ps
	ps2pdf main.ps

pdf: main.pdf

.PHONY: clean
clean: 
	-rm -f *.log *.aux *.bbl *.blg *.toc *.ps *.dvi *.pdf *.bak
	cd obrazky; make clean
	cd tabulky; make clean
	cd audio; make clean

.PHONY: full_clean
full_clean: clean
	cd obrazky; make full_clean
	cd tabulky; make full_clean
	cd audio; make full_clean

.PHONY: all
all: ps pdf obrazky tabulky audio


.PHONY: obrazky
obrazky:
	cd obrazky; make

.PHONY: tabulky
tabulky:
	cd tabulky; make

.PHONY: audio
audio:
	cd audio; make
