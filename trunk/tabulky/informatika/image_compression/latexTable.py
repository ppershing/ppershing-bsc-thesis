class LatexTable:
    def saveTable(filename, data):
        f = open(filename, 'w')
        header = reduce(lambda x,y:x+y , ['r' for col in data[0]])
        f.write('\\begin{tabular}{%s}\n' % header)
        for row in data:
            for i,x in enumerate(row):
                if (i):
                    f.write('&')
                f.write(str(x))
            f.write('\\\\\n')
        f.write('\\end{tabular}')
        f.close()
    saveTable = staticmethod(saveTable)
