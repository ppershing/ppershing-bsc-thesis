import random
from dct_mdct import DCT,MDCT

# size of processed transform
blockSize = 128

out_dct = open('dct.dat', 'w')

#dct processing
f = open('sample.dat', 'r')
for step in range(3):
    data = []
    for i in range(blockSize):
         data.append(float(f.readline()))
        
    dct_data = DCT.transform(data)
    for i in range(blockSize):
        dct_data[i] *= (1 + (random.random()-0.5)*0.6)
        
    dct_reconstructed = DCT.inverseTransform(dct_data)
    for i in range(blockSize):
        out_dct.write('%.7f\n' % (dct_reconstructed[i]))
        
out_dct.close()
f.close()

#mdct processing

tmp = MDCT.transform([0,0,1,1])
print tmp
tmp = MDCT.inverseTransform(tmp)
print tmp

# old window frame for mdct
old_data = [0.0 for i in range(blockSize)]
mdct_out_data = [0.0 for i in range(blockSize)]

out_mdct = open('mdct.dat', 'w')
f = open('sample.dat', 'r')
for step in range(3):
    data = []
    for i in range(blockSize):
         data.append(float(f.readline()))
        
    mdct_data = MDCT.transform(MDCT.window(old_data + data))
    for i in range(blockSize):
        mdct_data[i] *= (1 + (random.random()-0.5)*0.6)
        
    mdct_reconstructed = MDCT.window(MDCT.inverseTransform(mdct_data))
   
    if (step>0):        
        for i in range(blockSize):
            out_mdct.write('%.7f\n' %
            (mdct_reconstructed[i]+mdct_out_data[i]))
    
    old_data = data
    mdct_out_data = mdct_reconstructed[blockSize:]
