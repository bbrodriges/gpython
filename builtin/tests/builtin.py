# Copyright 2018 The go-python Authors.  All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

doc="abs"
assert abs(0) == 0
assert abs(10) == 10
assert abs(-10) == 10

doc="all"
assert all((0,0,0)) == False
assert all((1,1,0)) == False
assert all(["hello", "world"]) == True
assert all([]) == True

doc="any"
assert any((0,0,0)) == False
assert any((1,1,0)) == True
assert any(["hello", "world"]) == True
assert any([]) == False

doc="chr"
assert chr(65) == "A"
assert chr(163) == "£"
assert chr(0x263A) == "☺"

doc="compile"
code = compile("pass", "<string>", "exec")
assert code is not None
# FIXME

doc="divmod"
assert divmod(34,7) == (4, 6)

doc="eval"
# smoke test only - see vm/tests/builtin.py for more tests
assert eval("1+2") == 3

doc="exec"
# smoke test only - see vm/tests/builtin.py for more tests
glob = {"a":100}
assert exec("b = a+100", glob) == None
assert glob["b"] == 200

doc="getattr"
class C:
    def __init__(self):
        self.potato = 42
c = C()
assert getattr(c, "potato") == 42
assert getattr(c, "potato", 43) == 42
assert getattr(c, "sausage", 43) == 43

doc="globals"
a = 1
assert globals()["a"] == 1

doc="hasattr"
assert hasattr(c, "potato")
assert not hasattr(c, "sausage")

doc="len"
assert len(()) == 0
assert len((1,2,3)) == 3
assert len("hello") == 5
assert len("£☺") == 2

doc="locals"
def fn(x):
    assert locals()["x"] == 1
fn(1)

doc="next no default"
def gen():
    yield 1
    yield 2
g = gen()
assert next(g) == 1
assert next(g) == 2
ok = False
try:
    next(g)
except StopIteration:
    ok = True
assert ok, "StopIteration not raised"

doc="next with default"
g = gen()
assert next(g, 42) == 1
assert next(g, 42) == 2
assert next(g, 42) == 42
assert next(g, 42) == 42

doc="next no default with exception"
def gen2():
    yield 1
    raise ValueError("potato")
g = gen2()
assert next(g) == 1
ok = False
try:
    next(g)
except ValueError:
    ok = True
assert ok, "ValueError not raised"

doc="next with default and exception"
g = gen2()
assert next(g, 42) == 1
ok = False
try:
    next(g)
except ValueError:
    ok = True
assert ok, "ValueError not raised"

doc="ord"
assert 65 == ord("A")
assert 163 == ord("£")
assert 0x263A == ord("☺")
assert 65 == ord(b"A")
ok = False
try:
    ord("AA")
except TypeError as e:
    if e.args[0] != "ord() expected a character, but string of length 2 found":
        raise
    ok = True
assert ok, "TypeError not raised"
try:
    ord(None)
except TypeError as e:
    if e.args[0] != "ord() expected string of length 1, but NoneType found":
        raise
    ok = True
assert ok, "TypeError not raised"

doc="pow"
assert pow(2, 10) == 1024
assert pow(2, 10, 17) == 4

doc="repr"
assert repr(5) == "5"
assert repr("hello") == "'hello'"

doc="print"
# FIXME - need io redirection to test
#print("hello world")
#print(1,2,3,sep=",",end=",\n")

doc="round"
assert round(1.1) == 1.0

doc="setattr"
class C: pass
c = C()
assert not hasattr(c, "potato")
setattr(c, "potato", "spud")
assert getattr(c, "potato") == "spud"
assert c.potato == "spud"

doc="__import__"
lib = __import__("lib")
assert lib.libfn() == 42
assert lib.libvar == 43
assert lib.libclass().method() == 44

doc="finished"
