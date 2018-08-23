// Copyright 2018 The go-python Authors.  All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Float objects

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
	Data   []byte
}

// Type of this Hash object
func (h Hash) Type() *Type {
	return HashType
}

// NewHash defines a new hash
func NewHash(name string, h hash.Hash, data []byte) *Hash {
	return &Hash{name, h, data}
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
	return NewBool(bytes.Equal(h.Data, b.Data)), nil
}

func (h Hash) M__ne__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(!bytes.Equal(h.Data, b.Data)), nil
}

func (h Hash) M__gt__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Data, b.Data) > 0), nil
}

func (h Hash) M__lt__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Data, b.Data) < 0), nil
}

func (h Hash) M__ge__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Data, b.Data) >= 0), nil
}

func (h Hash) M__le__(other Object) (Object, error) {
	b, ok := other.(Hash)
	if !ok {
		return NotImplemented, nil
	}
	return NewBool(bytes.Compare(h.Data, b.Data) <= 0), nil
}
