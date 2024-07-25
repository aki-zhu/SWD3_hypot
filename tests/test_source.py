import pytest 
import swd3_hypot.source as source

def test_sqrt():
    input = 4
    e_output = 2.0
    output = source.sqrt(input)
    assert output == e_output
    
def test_sqrt1():
    input = 9
    e_output = 3.0
    output = source.sqrt(input)
    assert output == e_output
    
def test_hyp_func():
    opp = 3 
    adj = 4
    e_output = 5
    output = source.hyp_func(opp, adj)
    assert output == e_output