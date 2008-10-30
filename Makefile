default: pdf

main.dvi: *.tex *.bib Makefile */*.tex code/*
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
main.pdf: Makefile *.ps
	ps2pdf main.ps

pdf: main.pdf

html: dvi 
	for i in * ; do if [ ! -d "$i"] ; then cp "$i" html ; fi ; done
	cd html ; latex2html -html_version 4.0 -no_navigation -no_subdir -info 0 main.tex ; cd ..

clean: 
	rm -f *.log *.aux *.bbl *.blg *.toc *.ps *.dvi

dist-clean:
	rm -f *.{log,aux,dvi,ps,pdf,toc,bbl,blg,slo,srs}

backup: 
	tar --create --force-local -zf zaloha/knizka-`date +%Y-%m-%d-%H\:%M`.tar.gz `ls -p| egrep -v /$ ` images/* code/*

all: ps pdf


booklet: main.ps
	cat main.ps | psbook | psnup -2 >main-booklet.ps

