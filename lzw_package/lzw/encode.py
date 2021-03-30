import numpy as np
from bitarray import bitarray
from bitarray import frozenbitarray


def lzw_encode(input_seq):
    #instantiate variables
    unit = 1 
    e_seq = []
    d = dict( zip( [frozenbitarray(np.binary_repr(x, unit)) for x in range(2**unit)], np.arange(2**unit)))

    #check input validity
    if input_seq == None or len(input_seq) == 0:
        return None
    elif not set(input_seq).issubset({'0', '1'}) and bool(input_seq):
            print("WARNING: only binary inputs are allowed")
            return None


    d_seq = frozenbitarray(input_seq)


    #begin algorthm
    p = d_seq[:unit]

    for i in range(1, int(len(d_seq)/unit)):
        
        c = d_seq[unit*i:unit*(i+1)]
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
    return ''.join(e_seq) 

#print(lzw_encode('1001110'))