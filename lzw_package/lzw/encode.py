import numpy as np
from bitarray import bitarray
from bitarray import frozenbitarray


def lzw_encode(input_seq):
    """ Encodes the input binary sequence with the LZW algorithm, a data compression
        method that leverages the presence of repeated “runs” of equal symbols in most
        sequence that appears.
        
        Args:
            input_seq (str) : Sequence of zeros and ones to be encoded
        
        Returns:
            str : The compressed sequence. It has length multiple of 3.
        
        Raises:
            "WARNING: only binary inputs are allowed" : It accepts only strings containing zeros and ones.
            "WARNING: dictionary capacity exceeded" : If the different patterns found in the string exceed 997 (different than 0 and 1), the output 3-bit code is not enough anymore. If you want to increase the capacity, increase the bits of the output.
   
    """
    #instantiate variables
    unit = 1 
    out_unit = 3 #hard-coded
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
            p = pc 
        else:
            if len(d) < int(''.join(['9']*out_unit)):
                d[pc] = len(d)+ 1
            else:
                print("WARNING: dictionary capacity exceeded")
                return None
            e_seq.append( '{0:03}'.format(d.get( p )) ) #'3' to be changed if you want to increase the output bits
            p = c
    e_seq.append( '{0:03}'.format(d.get( p )) ) # '3' to be changed if you want to increase the output bits
    
    return ''.join(e_seq) 

