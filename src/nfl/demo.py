import pytest


def get_numbers():
    numbers = range(0, 1_000_000)
    for number in numbers:
        yield number

n = get_numbers()
print(n)
print(next(n))
print(next(n))
print(next(n))
print(next(n))

@pytest.fixture
def test_file():
    f = open('myfile.txt', 'r')
    yield f
    f.close()

def read_data(test_file):
    pass