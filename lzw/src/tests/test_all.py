
import pytest
from src.lzw import lzw_encode, lzw_decode



def test_empty():
	arr = ''
	assert lzw_encode(arr)[0]  == None
	assert lzw_decode(arr)  == None


def test_None():
	arr = None
	assert lzw_encode(arr)[0]  == None
	assert lzw_decode(arr)  == None

@pytest.mark.parametrize('arr', [ '1', '1010', '10010111','0000111100001111001100110000111100001111'])
def test_encode_decode(arr):
	m, extra_bits = lzw_encode(arr)
	
	assert lzw_decode(m, extra_bits) == arr

@pytest.mark.parametrize('arr', [ '001', '001000', '001000258000002001003'])
def test_decode_encode(arr):
	m = lzw_decode(arr)
	assert lzw_encode(m)[0] == arr


@pytest.mark.parametrize('arr', [  '001000259000002001003', '259001000', '0012'])
def test_validity(arr):
	m = lzw_decode(arr)
	assert lzw_encode(m)[0] == None