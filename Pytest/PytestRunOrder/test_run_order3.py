import pytest


@pytest.mark.order(4)
def test_method9():
    print('Hello world')


@pytest.mark.order(3)
def test_method10():
    print('Hello Dhaka')


@pytest.mark.order(2)
def test_method11():
    print('Hello BITM')


@pytest.mark.order(1)
def test_method12():
    print('Hello PnT')
