import pytest


@pytest.fixture
def dummy_fixture():
    print("inside dummy fixture function")
    return "Hello!"
