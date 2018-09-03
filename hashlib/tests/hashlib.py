# Copyright 2018 The go-python Authors.  All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# FIXME Convert tests from cpython/Lib/test/test_hashlib.py

import hashlib
from libtest import *

def ftest(name, got, want):
    what = '%s got %r, want %r' % (name, got, want)
    assert got == want, what

doc="MD5"
ftest('new_md5_0', hashlib.new('md5', b'').hexdigest(), 'd41d8cd98f00b204e9800998ecf8427e')
ftest('new_md5_1', hashlib.new('md5', b'').digest(), b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~')
ftest('new_md5_2', hashlib.new('md5', b'abc').hexdigest(), '900150983cd24fb0d6963f7d28e17f72')
ftest('new_md5_3', hashlib.new('md5', b'abc').digest(), b'\x90\x01P\x98<\xd2O\xb0\xd6\x96?}(\xe1\x7fr')
ftest('new_md5_4', 
            hashlib.new('md5', b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789').hexdigest(),
            'd174ab98d277d9f5a5611c2c9f419d9f')
assertRaises(TypeError, hashlib.new, 'md5', 'abc')

ftest('md5_0', hashlib.md5().hexdigest(), 'd41d8cd98f00b204e9800998ecf8427e')
ftest('md5_1', hashlib.md5().digest(), b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~')
ftest('md5_2', hashlib.md5(b'abc').hexdigest(), '900150983cd24fb0d6963f7d28e17f72')
ftest('md5_3', hashlib.md5(b'abc').digest(), b'\x90\x01P\x98<\xd2O\xb0\xd6\x96?}(\xe1\x7fr')
ftest('md5_4', 
            hashlib.md5(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789').hexdigest(),
            'd174ab98d277d9f5a5611c2c9f419d9f')
assertRaises(TypeError, hashlib.md5, 'abc')

doc="SHA1"
ftest('new_sha1_0', hashlib.new('sha1', b'').hexdigest(), 'da39a3ee5e6b4b0d3255bfef95601890afd80709')
ftest('new_sha1_1', hashlib.new('sha1', b'').digest(), b'\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t')
ftest('new_sha1_2', hashlib.new('sha1', b'abc').hexdigest(), 'a9993e364706816aba3e25717850c26c9cd0d89d')
ftest('new_sha1_3', hashlib.new('sha1', b'abc').digest(), b'\xa9\x99>6G\x06\x81j\xba>%qxP\xc2l\x9c\xd0\xd8\x9d')
ftest('new_sha1_4',
            hashlib.new('sha1', b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq').hexdigest(),
            '84983e441c3bd26ebaae4aa1f95129e5e54670f1')
assertRaises(TypeError, hashlib.new, 'sha1', 'abc')

ftest('sha1_0', hashlib.sha1(b'').hexdigest(), 'da39a3ee5e6b4b0d3255bfef95601890afd80709')
ftest('sha1_1', hashlib.sha1(b'').digest(), b'\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t')
ftest('sha1_2', hashlib.sha1(b'abc').hexdigest(), 'a9993e364706816aba3e25717850c26c9cd0d89d')
ftest('sha1_3', hashlib.sha1(b'abc').digest(), b'\xa9\x99>6G\x06\x81j\xba>%qxP\xc2l\x9c\xd0\xd8\x9d')
ftest('sha1_4',
            hashlib.sha1(b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq').hexdigest(),
            '84983e441c3bd26ebaae4aa1f95129e5e54670f1')
assertRaises(TypeError, hashlib.sha1, 'abc')

doc="finished"
