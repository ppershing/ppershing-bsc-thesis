from dct import DCT
import pprint
import math
from latexTable import LatexTable

# original image
block1 = \
[[139,144,149,153,155,155,155,155],
[144,151,153,156,159,156,156,156],
[150,155,160,163,158,156,156,156],
[159,161,162,160,160,159,159,159],
[159,160,161,162,162,155,155,155],
[161,161,161,161,160,157,157,157],
[162,162,161,163,162,157,157,157],
[162,162,161,161,163,158,158,158]]

#quantizer table
quantizer = \
[[16,11,10,16,24,40,51,61],
[12,12,14,19,26,58,60,55],
[14,13,16,24,40,57,69,56],
[15,17,22,29,51,87,80,62],
[18,22,37,56,68,109,103,77],
[24,35,55,64,81,104,113,92],
[49,64,78,87,103,121,120,101],
[72,92,95,98,112,100,103,99]]

#normalize
block2 = [[ x-128 for x in row] for row in block1]

#compute dct
block3 = DCT.transform2D(block2)
block4 = DCT.normalize(block3)

#quantize
block5 = [[ int(round(x/qx)) for x,qx in zip(row,qrow)] 
                for row,qrow in zip(block4,quantizer)]

#dequantize
block6 = [[ x*qx for x,qx in zip(row,qrow)] 
                for row,qrow in zip(block5,quantizer)]

#normalize before inverse transform
block7 = DCT.normalize(block6)
#inverse transform
block8 = DCT.inverseTransform2D(block7)

#shift and round
block9 = [[ int(x+128.5) for x in row] for row in block8]

LatexTable.saveTable('original.tbl', block1)
LatexTable.saveTable('quantization.tbl', quantizer)
LatexTable.saveTable('after_dct.tbl', [[ '%.1f'%x for x in row]for row in block4])
LatexTable.saveTable('after_quantization.tbl', block5)
LatexTable.saveTable('after_dequantization.tbl', block6)
LatexTable.saveTable('final.tbl', block9)
