from task01 import main


def check_remainder():
    result = main(500, 200)
    assert 300 == result['balance']

def check_negative():
    result = main(500, -1)
    assert 500 == result['balance']

def test03(input):
    assert input == 1

def test04(input):
    assert input == 1

def test05(input):
    assert input == 1