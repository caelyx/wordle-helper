import pytest
import wrdl


def test_one():
    class args:
        green = "....e"
        yellow = "toh"
        grey = "iravuc"

    assert wrdl.search(args) == ["those"]


def test_zero():
    class args:
        green = "....z"
        yellow = "toh"
        grey = "iravuc"

    assert wrdl.search(args) == []


def test_several():
    class args:
        green = "....e"
        yellow = "bd"
        grey = "zxcv"

    assert wrdl.search(args) == ["adobe", "badge", "budge", "abide", "bride", "abode", "blade"]
