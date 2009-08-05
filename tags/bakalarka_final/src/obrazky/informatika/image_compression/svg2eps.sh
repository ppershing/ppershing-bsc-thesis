INKSCAPE="/cygdrive/c/Program Files/Inkscape/inkscape.exe"

CYG_WD=`pwd`
DOS_WD=`cygpath -d $CYG_WD`
file=$1
echo "Converting $file.svg to $file.eps"

"${INKSCAPE}" "$DOS_WD/$file.svg" --export-eps="$DOS_WD/$file.eps"
