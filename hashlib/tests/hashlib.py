# Copyright 2018 The go-python Authors.  All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# FIXME Convert tests from cpython/Lib/test/test_hashlib.py

import hashlib
from libtest import *

def ftest(name, got, want):
    what = '%s got %r, want %r' % (name, got, want)
    assert got == want, what

doc='Rich comparision'
assertEqual(hashlib.md5(b'abc'), hashlib.md5(b'abc'))

doc="MD5"  
ftest('new_md5_0', hashlib.new('md5', b'').hexdigest(), 'd41d8cd98f00b204e9800998ecf8427e')
ftest('new_md5_1', hashlib.new('md5', b'abc').hexdigest(), '900150983cd24fb0d6963f7d28e17f72')
ftest('mew_md5_2', 
            hashlib.new('md5', b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789').hexdigest(),
            'd174ab98d277d9f5a5611c2c9f419d9f')
assertRaises(TypeError, hashlib.new, 'md5', 'abc')

ftest('md5_0', hashlib.md5().hexdigest(), 'd41d8cd98f00b204e9800998ecf8427e')
ftest('md5_1', hashlib.md5(b'abc').hexdigest(), '900150983cd24fb0d6963f7d28e17f72')

doc="finished"
