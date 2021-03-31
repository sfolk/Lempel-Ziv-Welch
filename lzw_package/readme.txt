The Lempel–Ziv–Welch (LZW) algorithm is a well known data compression
method that leverages the presence of repeated “runs” of equal symbols in most
sequence that appears (e.g., in text).

We use a Python library (e.g., bitarray) allowing easy low-level manipulation of
bits and bytes.
The aim of this project is to implement two functions, lzw_encode and
lzw_decode, that, given a binary sequence as argument, return the encoded
(resp., decoded) sequence using the LZW algorithm.

Notes:
I chose to use bits as units, since taking the bytes would require the input to be multiple of 8. 
An older version of this code used the bytes and returned the number of 'extra bits' added in order to make the input compatible.
The extra-bits information was essential to be returned, in order to decode correctly.
