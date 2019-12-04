import pytest
from Hello_World import *

#This is a test for hello jenkins, full auto

def test_hello():
    result = hello()
    assert result == "Hello!"
