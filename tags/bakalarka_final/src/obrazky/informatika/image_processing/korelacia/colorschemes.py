def Gray(x):
    return (x, x, x)

def InverseGray(x):
    return (1-x, 1-x, 1-x)

def BlueGreenRed(x):
    if (x>0.5):
        return (2.0*x-1,2*(1-x),0)
    else:
        return (0, 2*x, 2.0*(1-x)-1)
