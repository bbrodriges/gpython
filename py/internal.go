// Internal interface for use from Go
//
// See arithmetic.go for the auto generated stuff

package py

import (
	"fmt"
)

// Bool is called to implement truth value testing and the built-in
// operation bool(); should return False or True. When this method is
// not defined, __len__() is called, if it is defined, and the object
// is considered true if its result is nonzero. If a class defines
// neither __len__() nor __bool__(), all its instances are considered
// true.
func MakeBool(a Object) Object {
	if _, ok := a.(Bool); ok {
		return a
	}

	if A, ok := a.(I__bool__); ok {
		res := A.M__bool__()
		if res != NotImplemented {
			return res
		}
	}

	if B, ok := a.(I__len__); ok {
		res := B.M__len__()
		if res != NotImplemented {
			return MakeBool(res)
		}
	}

	return True
}

// Index the python Object returning an int
//
// Will raise TypeError if Index can't be run on this object
func Index(a Object) int {
	A, ok := a.(I__index__)
	if ok {
		return A.M__index__()
	}

	// FIXME should be TypeError
	panic(fmt.Sprintf("TypeError: unsupported operand type(s) for index: '%s'", a.Type().Name))
}

// Return the result of not a
func Not(a Object) Object {
	switch MakeBool(a) {
	case False:
		return True
	case True:
		return False
	}
	panic("bool() didn't return True or False")
}