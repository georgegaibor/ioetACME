import sys
import pytest
from app import main


def test():
    return pytest.main(["-v", "./app/test"])


if __name__ == "__main__":
    if sys.argv[1] == "test":
        test()
    else:
        main(sys.argv)
