
import pytest
import numpy as np
from lzw.encode import lzw_encode
from lzw.decode import lzw_decode
@pytest.mark.parametrize('arr', [ '', None])
def test_empty(arr):
	assert lzw_encode(arr)  == None
	assert lzw_decode(arr)  == None

@pytest.mark.parametrize('arr', [ '1', '1010', '10010111','0000111100001111001100110000111100001111'])
def test_encode_decode(arr):
	m = lzw_encode(arr)
	
	assert lzw_decode( m ) == arr




@pytest.mark.parametrize('arr', [  '001000259000002001003', '259001000', '0012', 'abc'])
def test_validity(arr):
	assert lzw_decode(arr)== None

@pytest.mark.parametrize('arr', [  'abcca', '259001000', ''.join([np.binary_repr(x, 10) for x in range(2**10)]) ])
def test_validity_encoder(arr):
	assert lzw_encode(arr) == None