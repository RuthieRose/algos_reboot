from example import example
import pytest

def test_example(capfd):
    example.example()
    assert capfd.readouterr().out == 'hello algo world\n'
