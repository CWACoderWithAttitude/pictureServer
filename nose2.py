from mynum import *
import nose
 
def test_add_integers():
    assert add(5, 3) == 8
 
def test_add_floats():
    assert add(1.5, 2.5) == 4
 
def test_add_strings():
    nose.tools.assert_raises(AssertionError, add, 'paul', 'carol') 
#// To throw one of the expected exception to pass
 
if __name__ == '__main__':   
    nose.run()
