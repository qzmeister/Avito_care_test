import pytest

def run_tests():
    test_files = ['test_1.py', 'test_2.py', 'test_3.py']

    for test_file in test_files:
        pytest.main([test_file])


if __name__ == "__main__":
    run_tests()
