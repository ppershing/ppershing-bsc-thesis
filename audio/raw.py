import array;
import os;

class RawAudio:
    def load(filename):
        f = open(filename, 'r')
        a = array.array('d')
        statinfo = os.stat(filename)
        a.read(f,statinfo.st_size/8)
        f.close()
        return a.tolist()

    load = staticmethod(load)

    def save(filename, data):
        a = array.array('d', data)
        f = open(filename, 'w')
        a.tofile(f)
        f.close()
        
    save = staticmethod(save)
