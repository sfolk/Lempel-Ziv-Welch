import numpy as np
from bitarray import bitarray
from bitarray import frozenbitarray


def lzw_decode(e_seq ):
    """ Decodes the input sequence with the LZW algorithm, a data compression
        method that leverages the presence of repeated “runs” of equal symbols in most
        sequence that appears.
        
        Args:
            input_seq (str) : The code to be decompressed. Must be composed of triplets of digits.
        
        Returns:
            str : The binary decompressed sequence. 
        
        Raises:
            "WARNING: the input sequence is not a multiple of 3'" : It accepts only strings with length multiple of three.
            "WARNING: characters are not allowed" : The input must contain only digits and no characters.
            "WARNING: the input code is not valid " : The code must be decomposable by LZW decoding algorithm. A triplet cannot refer to dictionary entries that are not yet found.

    """
    #check input validity
    if e_seq == None or len(e_seq) == 0:
        return None

    #instantiate variables
    cod_unit = 3
    input_unit = 1
    d_seq = []
    d = dict( zip( np.arange(2**input_unit), [np.binary_repr(x, input_unit) for x in range(2**input_unit)] ) )
    
    #check input validity
    if  (len(e_seq) % cod_unit != 0 ):
        print('WARNING: the input sequence is not a multiple of 3')
        return None
    elif  (e_seq.isupper() or e_seq.islower()):
        print("WARNING: characters are not allowed")
        return None
    
    #begin decode
    p = int(e_seq[: cod_unit])

    for i in range(1, int(len(e_seq)/cod_unit)):

        c = int(e_seq[ cod_unit * i     : cod_unit * (i+1) ])

        if d.get( p ) != None :
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


