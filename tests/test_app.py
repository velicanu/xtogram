from app import main
from utils import DEFAULT_CONFIG


def test_main():
    expected = DEFAULT_CONFIG
    actual = main(DEFAULT_CONFIG)
    assert actual == expected
