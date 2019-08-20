import testhw

def test_zebra():
    assert 'zebra' == testhw.last_alph(['cow', 'snake', 'goat', 'lion', 'zebra', 'mongoose'])


def test_cobra():
    assert 'cobra' == testhw.last_alph(['cobra','bison', 'ardvark', 'ant', 'canary'])


def test_something_returned():
    assert testhw.last_alph(['cow', 'snake', 'goat']) is not None

def test_returned_string():
    assert type(testhw.last_alph(['cow', 'snake', 'goat', 'lion', 'zebra', 'mongoose']))==str
