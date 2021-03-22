
from bitarray import bitarray, frozenbitarray
import numpy as np

def lzw_encode(input_seq):

    e_seq = []
    d = dict( zip( [frozenbitarray(np.binary_repr(x, 8)) for x in range(2**8)], np.arange(2**8)))
    
    d_seq = bitarray(input_seq)
    if  (len(input_seq) % 8 != 0 ):
        print('WARNING: the input sequence is not a multiple of 8, {} will be added to the end of the sting'.format(d_seq.fill()))
    d_seq = frozenbitarray(d_seq)

    p = d_seq[:8]
    
    
    for i in range(1, int(len(d_seq)/8)):
        
        c = d_seq[8*i:8*(i+1)]
        pc = p+c

        if d.get( pc ) != None :
            #if the sequence was already in the dictionary 
            print(pc,' found in dict, in place',  d.get( pc )  )
            p = pc 
        else:
            d[pc] = len(d)+ 1
            print('saved ',pc,' to dictionary in position ',  2**8 + i)
            e_seq.append( d.get( p ) )
            p = c

    e_seq.append( d.get( p ) )
    return e_seq

#input : 00000001 00000011  00000001 00000011 00000001 00000011 
e_seq = lzw_encode('0000000100000011000000010000001100000001000000110000000100000011')

print(e_seq)

def lzw_encode(e_seq):

    return 0
