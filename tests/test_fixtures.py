"""

The golden reference: https://docs.pytest.org/en/latest/fixture.html#usefixtures

0. A fixture function can be passed as a parameter to a test case and the return value of fixture can be accessed in the
test case by accessing the fixture function name like a variable.

1. One can specify the scope of a fixture, especially useful for sharing expensive connections.
You can run the whole module with scope=module defined vs default function scope, you can see in the scope setting,
fixture is only called once, the other one is run for every test case.

2. One can also put all fixtures in a conftest.py file for better organization. as shown be dummy_fixture.

3. By using yield we can run the tear down part at the end of the scope of fixture



"""

# content of ./test_smtpsimple.py
import pytest


@pytest.fixture(scope="module")
def smtp_connection():
    import smtplib
    print("inside smtp connection fixture")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    # by using yield we can run the tear down part at the end of the scope of fixture
    print("teardown smtp")
    smtp_connection.close()


def test_ehlo(smtp_connection):
    """
    This example shows how to pass fixture functions as paramter to test case.
    Note that the fixture return value is accessible as the function name.

    :param smtp_connection: fixture function name
    :type smtp_connection: function
    """
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # for demo purposes


def test_ehlo2(smtp_connection):
    """
    This example shows how to pass fixture functions as paramter to test case.
    Note that the fixture return value is accessible as the function name.

    :param smtp_connection: fixture function name
    :type smtp_connection: function
    """
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # for demo purposes


def test_dummy(dummy_fixture, smtp_connection):
    print(dummy_fixture)
    assert dummy_fixture == "Hello!"
    assert 0  # fail it for demo purpose
