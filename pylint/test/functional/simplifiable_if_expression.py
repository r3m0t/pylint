"""Test that some if expressions can be simplified."""

# pylint: disable=missing-docstring, invalid-name


def test_simplifiable_1(arg):
    # Simple test that can be replaced by bool(arg)
    return True if arg else False # [simplifiable-if-expression]

def test_simplifiable_2(arg):
    # Simple test that can be replaced by not arg
    return False if arg else True # [simplifiable-if-expression]

def test_simplifiable_3(arg):
    # Simple test that can be replaced by arg == 1
    return True if arg == 1 else False # [simplifiable-if-expression]

def test_simplifiable_4(arg):
    # Simple test that can be replaced by not (arg == 1)
    return False if arg == 1 else True # [simplifiable-if-expression]
