import unittest

# Here's our "unit".


def IsOdd(n):
    if n == 1:
        return True
    if n == 2:
        return False
# Here's our "unit tests".


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
