import numpy as np
from bitarray import bitarray
from bitarray import frozenbitarray


def lzw_decode(e_seq ):

    if e_seq == None or len(e_seq) == 0:
        return None

    cod_unit = 3
    input_unit = 1

    d_seq = []
    d = dict( zip( np.arange(2**input_unit), [np.binary_repr(x, input_unit) for x in range(2**input_unit)] ) )
    
    if  (len(e_seq) % cod_unit != 0 ):
        print('WARNING: the input sequence is not a multiple of 3')
        return None

    elif  (e_seq.isupper() or e_seq.islower()):
        print("WARNING: only binary inputs are allowed")
        return None
        
    p = int(e_seq[: cod_unit])

    for i in range(1, int(len(e_seq)/cod_unit)):


        c = int(e_seq[ cod_unit * i     : cod_unit * (i+1) ])

        
        if d.get( p ) != None :
            
            #if the sequence was already in the dictionary 
            d_seq.append(d.get( p ))
            if d.get(c):
                d[len(d)+1] = str(d.get( p )) + str(d.get(c)[:input_unit])
            
            elif c==len(d)+1:
                d[len(d)+1] = str(d.get( p )) + str(d.get(p)[:input_unit])
            else:
                print("WARNING: the input code is not valid ")
                return None
            p = c

        else:
            print("WARNING: the input code is not valid")
            return None


    d_seq.append(d.get( p ))
    output_string = ''.join(d_seq)
    
    return output_string


