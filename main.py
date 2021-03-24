from bitarray import bitarray, frozenbitarray
import numpy as np


def lzw_encode(input_seq):

    if input_seq == None or len(input_seq) == 0:
        return None, None


    e_seq = []
    d = dict( zip( [frozenbitarray(np.binary_repr(x, 8)) for x in range(2**8)], np.arange(2**8)))
    
    d_seq = bitarray(input_seq)
    
    n_added = d_seq.fill()

    if n_added :
        print( "WARNING!! In the following result, {} bits were added ".format(n_added))

    d_seq = frozenbitarray(d_seq)

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


def lzw_decode(e_seq, extra_bits = 0 ):

    if e_seq == None or len(e_seq) == 0:
        return None

    cod_unit = 3

    d_seq = []
    d = dict( zip( np.arange(2**8), [np.binary_repr(x, 8) for x in range(2**8)] ) )
    
    if  (len(e_seq) % cod_unit != 0 ):
        print('WARNING: the input sequence is not a multiple of 3, the last {} bits will be cutted'.format( len(e_seq) // cod_unit))

    p = int(e_seq[: cod_unit])

    for i in range(1, int(len(e_seq)/cod_unit)):

        c = int(e_seq[ cod_unit * i     : cod_unit * (i+1) ])
        #print('here is the c', c)

        if d.get( p ) != None :
            
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
                print("WARNING: the input code is not valid because the index {} wasn't in dictionary".format(c))
                return None
            p = c

        else:
            print("WARNING: the input code is not valid because the index {} wasn't in dictionary".format(p))
            return None

#input : 00000001 00000011  00000001 00000011 00000001 00000011 
e_seq = lzw_encode('0000000100000011000000010000001100000001000000110000000100000011')[0]



#d_seq = lzw_decode('001000258')
#print(d_seq)

