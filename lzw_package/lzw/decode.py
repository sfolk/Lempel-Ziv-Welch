import numpy as np
from bitarray import bitarray
from bitarray import frozenbitarray


def lzw_decode(e_seq, extra_bits = 0 ):

    if e_seq == None or len(e_seq) == 0:
        return None

    cod_unit = 3

    d_seq = []
    d = dict( zip( np.arange(2**8), [np.binary_repr(x, 8) for x in range(2**8)] ) )
    
    if  (len(e_seq) % cod_unit != 0 ):
        print('WARNING: the input sequence is not a multiple of 3')
        return None
        
    p = int(e_seq[: cod_unit])

    for i in range(1, int(len(e_seq)/cod_unit)):


        c = int(e_seq[ cod_unit * i     : cod_unit * (i+1) ])
        #print('here is the c', c)

        
        if d.get( p ) != None :
            print(d.get( p ))
            
            #if the sequence was already in the dictionary 
            #print(d.get( p ),' found p in dict, in place',  p  )
            d_seq.append(d.get( p ))
            if d.get(c):
                print(d.get( c ),' found c in dict, in place',  c  )
                d[len(d)+1] = str(d.get( p )) + str(d.get(c)[:8])
                #print('saved ',str(d.get( p )) + str(d.get(c)[:8]),' to dictionary in position ',  len(d))
            
            elif c==len(d)+1:
                #print('here is the p', p)
                d[len(d)+1] = str(d.get( p )) + str(d.get(p)[:8])
                #print('saved ', str(d.get( p )) + str(d.get(p)[:8]),' to dictionary in position ',  len(d))
            else:
                print("WARNING: the input code is not valid ")
                return None
            p = c

        else:
            print("WARNING: the input code is not valid")
            return None


    d_seq.append(d.get( p ))
    output_string = ''.join(d_seq)
    #print('decoded value:', ''.join(d_seq) )
    
    return output_string[: (len(output_string)-extra_bits)]
