import numpy as np
from bitarray import bitarray
from bitarray import frozenbitarray


def lzw_encode(input_seq):

    if input_seq == None or len(input_seq) == 0:
        return None, None

    unit = 8 
    e_seq = []
    d = dict( zip( [frozenbitarray(np.binary_repr(x, 8)) for x in range(2**8)], np.arange(2**8)))
    
    if len(input_seq) % unit != 0:
        d_seq = bitarray(input_seq)
        n_added = d_seq.fill()  
        print( "WARNING!! In the following result, {} bits were added ".format(n_added))
        d_seq = frozenbitarray(d_seq)
    else:
        n_added = 0
        d_seq = frozenbitarray(input_seq)

    p = d_seq[:8]
    
    for i in range(1, int(len(d_seq)/8)):
        
        c = d_seq[8*i:8*(i+1)]
        pc = p+c

        if d.get( pc ) != None :
            #if the sequence was already in the dictionary 
            #print(pc,' found in dict, in place',  d.get( pc )  )
            p = pc 
        else:
            d[pc] = len(d)+ 1
            #print('saved ',pc,' to dictionary in position ',  2**8 + i)
            e_seq.append( '{0:03}'.format(d.get( p )) )
            p = c

    e_seq.append( '{0:03}'.format(d.get( p )) )
    #print(  'encoded sequence', ''.join(e_seq))
    return ''.join(e_seq) , n_added

