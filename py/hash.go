// Copyright 2018 The go-python Authors.  All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Hash objects

package py

import (
	"bytes"
	"fmt"
	"hash"
)

var HashType = ObjectType.NewType("hash", "a hash object implementing the given hash function", nil, nil)

type Hash struct {
	Name   string
	Hasher hash.Hash
}

// Type of this Hash object
func (h Hash) Type() *Type {
	return HashType
}

// NewHash defines a new hash
func NewHash(name string, h hash.Hash) *Hash {
	return &Hash{name, h}
}

func (h *Hash) M__str__() (Object, error) {
	return h.M__repr__()
}

func (h *Hash) M__repr__() (Object, error) {
	return String(fmt.Sprintf("<%s HASH object @ %v>", h.Name, h)), nil
}

func (h Hash) M__eq__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Equal(h.Hasher.Sum(nil), b.Hasher.Sum(nil))), nil
}

func (h Hash) M__ne__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(!bytes.Equal(h.Hasher.Sum(nil), b.Hasher.Sum(nil))), nil
}

func (h Hash) M__gt__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Hasher.Sum(nil), b.Hasher.Sum(nil)) > 0), nil
}

func (h Hash) M__lt__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Hasher.Sum(nil), b.Hasher.Sum(nil)) < 0), nil
}

func (h Hash) M__ge__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Hasher.Sum(nil), b.Hasher.Sum(nil)) >= 0), nil
}

func (h Hash) M__le__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Hasher.Sum(nil), b.Hasher.Sum(nil)) <= 0), nil
}

func init() {
	HashType.Dict["update"] = MustNewMethod("update", func(self Object, arg Object) (Object, error) {
		data, err := BytesFromObject(arg)
		if err != nil {
			return self, err
		}
		_, err = self.(*Hash).Hasher.Write(data)
		return self, err
	}, 0, "update(arg) -> Update the hash object with the object arg, which must be interpretable as a buffer of bytes. Repeated calls are equivalent to a single call with the concatenation of all the arguments: m.update(a); m.update(b) is equivalent to m.update(a+b).")

	HashType.Dict["digest"] = MustNewMethod("digest", func(self Object) (Object, error) {
		return Bytes(self.(*Hash).Hasher.Sum(nil)), nil
	}, 0, "digest() -> Return the digest of the data passed to the update() method so far. This is a bytes object of size digest_size which may contain bytes in the whole range from 0 to 255.")

	HashType.Dict["hexdigest"] = MustNewMethod("hexdigest", func(self Object) (Object, error) {
		return String(fmt.Sprintf("%x", self.(*Hash).Hasher.Sum(nil))), nil
	}, 0, "hexdigest() -> Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.")

	// FIXME find a way to implement copy() method

	HashType.Dict["name"] = &Property{
		Fget: func(self Object) (Object, error) {
			return String(self.(*Hash).Name), nil
		},
	}

	HashType.Dict["block_size"] = &Property{
		Fget: func(self Object) (Object, error) {
			return Int(self.(*Hash).Hasher.BlockSize()), nil
		},
	}

	HashType.Dict["digest_size"] = &Property{
		Fget: func(self Object) (Object, error) {
			return Int(self.(*Hash).Hasher.Size()), nil
		},
	}
}

var _ richComparison = new(Hash)
