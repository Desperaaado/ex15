from nose.tools import *
from ex15.ex15_stack import *

def setup():
    print("==ex15_stack==")

def teardown():
    print("TEAR DOWN!")

def test_push():
    colors = Stack()
    colors.push('apple')
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    colors.dump()

def test_pop():
    colors = Stack()
    # assert colors.pop() == None
    colors.push('apple')
    assert colors.pop() == 'apple'
    colors.push('banana')
    colors.push('canada')
    assert colors.pop() == 'canada'
    colors.push('duck')
    assert colors.pop() == 'duck'
    colors.dump()