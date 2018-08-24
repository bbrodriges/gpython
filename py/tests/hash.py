# Copyright 2018 The go-python Authors.  All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import hashlib

doc="str"
s = str(hashlib.new("md5"))
assert "<md5 HASH object @ " in s

doc="repr"
s = repr(hashlib.new("md5"))
assert "<md5 HASH object @ " in s

doc="eq"
h1 = hashlib.new("md5", data=b'hello')
h2 = hashlib.new("md5", data=b'hello')
assert h1 == h2

doc="ne"
h1 = hashlib.new("md5", data=b'hello')
h2 = hashlib.new("md5", data=b'world')
assert h1 != h2

doc="lt"
h1 = hashlib.new("md5", data=b'two')
h2 = hashlib.new("md5", data=b'three')
assert h1 < h2

doc="gt"
h1 = hashlib.new("md5", data=b'eight')
h2 = hashlib.new("md5", data=b'one')
assert h1 > h2

doc="le"
h1 = hashlib.new("md5", data=b'one')
h2 = hashlib.new("md5", data=b'two')
assert h1 <= h2

doc="ge"
h1 = hashlib.new("md5", data=b'two')
h2 = hashlib.new("md5", data=b'one')
assert h1 >= h2

doc="finished"
