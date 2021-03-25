The encoding and decoding functions can be accessed by installing the package:


From a terminal open on this folder, type  $pip install -e lzw_folchini/

usage:
	$ python
	>>> from src.lzw import lzw_encode, lzw_decode
	>>> a = lzw_encode('10000100')
	>>> print(lzw_decode(a))



