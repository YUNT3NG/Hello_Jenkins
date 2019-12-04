import pytest
from Hello_World import *

def test_hello():
    result = hello()
    assert result == "Hello!"