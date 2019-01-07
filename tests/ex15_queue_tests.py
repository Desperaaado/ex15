from nose.tools import *
from ex15.ex15_queue import *

def setup():
    print("==ex15_queue==")

def teardown():
    print("TEAR DOWN!")

def test_push():
    colors = Queue()
    colors.push('apple')
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    colors.dump()

def test_unshift():
    colors = Queue()
    colors.push('apple')
    colors.push('banana')
    colors.push('canada')
    assert colors.unshift() == 'apple'
    result = colors.dump()
    answer = ['banana', 'canada']
    assert result == answer