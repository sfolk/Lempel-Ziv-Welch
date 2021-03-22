
from bitarray import bitarray
import numpy as np

def lzw_encode(input_seq):

    d_seq = bytes(input_seq, 'utf-8')
    e_seq = []
    d = dict( zip( [bytes(np.binary_repr(x, 8), 'utf-8') for x in range(2**8)], np.arange(2**8)))

    if  (len(d_seq) % 8 != 0 ):
        print('WARNING: the input sequence is not a multiple of 8, will be cut to length', len(d_seq) // 8)

    p = d_seq[:8]
    
    for i in range(1, int(len(d_seq)/8)):
        
        c = d_seq[8*i:8*(i+1)]
        pc = bytes(str(p, 'utf-8')+str(c, 'utf-8'), 'utf-8')

        if d.setdefault( pc, len(d)+1 ) != 2**8 + i:
            #if the sequence was already in the dictionary (add it if it wasn't)
            p = pc 
        else:
            e_seq.append( d.get( p ) )
            p = c

    e_seq.append( d.get( p ) )
    return e_seq

#input : 00000001 00000011  00000001 00000011 
e_seq = lzw_encode('00000001000000110000000100000011')

print(e_seq)

def lzw_encode(e_seq):

    return d_seq
