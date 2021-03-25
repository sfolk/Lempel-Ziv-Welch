The encoding and decoding functions can be accessed by installing the package:


From a terminal open on this folder, type  $pip install -e lzw_folchini/

usage:
	$ python
	>>> from lzw.encode import lzw_encode
	>>> from lzw.decode import lzw_decode
	>>> a = lzw_encode('10000100')
	>>> print(lzw_decode(a))



