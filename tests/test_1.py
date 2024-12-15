import pytest
import random


@pytest.mark.skip
def test_aaa():
    assert 1 == 1


@pytest.mark.smoke
def test_bbb():
    assert 1 == 2


@pytest.mark.regression
def test_ccc():
    assert 2 == 2


def test_equal(generate_code):
    assert 1 == generate_code




