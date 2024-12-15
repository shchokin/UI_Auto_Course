import pytest
import random


@pytest.fixture
def generate_code():
    return random.randint(0, 10)
