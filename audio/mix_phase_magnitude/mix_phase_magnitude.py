from dif import DIF
from raw import RawAudio
from bitutils import BitUtils

data = RawAudio.load('source.raw');
data2 = RawAudio.load('source2.raw');
print "data loaded"

blockSize = 65536

blockCount = min(len(data)/blockSize, len(data2)/blockSize)
def Mix(x, y, phase, magnitude):
    z = 1
    if magnitude: # use second magnitude
        z *= abs(y)
    else:
        z *= abs(x)

    if phase:        
        z *= y / abs(y)
    else:
        z *= x / abs(x)
    return complex(z)
        
def Process(data, data2, MixFunction):
    data_out = []
    for i in range(blockCount):
        print "processing ", i*blockSize
        block = data[i*blockSize:(i+1)*blockSize]
        block2 = data2[i*blockSize:(i+1)*blockSize]
        
        DIF.transformInPlace(block)
        DIF.transformInPlace(block2)

        block_mixed = [ MixFunction(x, y).conjugate() \
                        / blockSize for x, y in zip(block, block2) ]
        DIF.transformInPlace(block_mixed)
        data_out += [ x.real for x in block_mixed ]
    return data_out

RawAudio.save('p1m1.raw', Process(data, data2,
                lambda x,y: complex(x) ))
RawAudio.save('p1m2.raw', Process(data, data2, 
                lambda x,y: complex(x) / abs(x) * abs(y)))
RawAudio.save('p2m1.raw', Process(data, data2,
                lambda x,y: complex(y) / abs(y) * abs(x)))
RawAudio.save('p2m2.raw', Process(data, data2,
                lambda x,y: complex(y)))
RawAudio.save('p1mc.raw', Process(data, data2,
                lambda x,y: complex(x)/abs(x) * 10.0 ))
RawAudio.save('pcm1.raw', Process(data, data2,
                lambda x,y: complex(1) * abs(x)))
RawAudio.save('p2mc.raw', Process(data, data2,
                lambda x,y: complex(y)/abs(y) * 10.0 ))
RawAudio.save('pcm2.raw', Process(data, data2,
                lambda x,y: complex(1) * abs(y)))
