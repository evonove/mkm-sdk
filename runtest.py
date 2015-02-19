import unittest
import sys


if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='.')
    testRunner = unittest.runner.TextTestRunner()
    result = testRunner.run(tests)
    sys.exit(len(result.errors)+len(result.failures))
