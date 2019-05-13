import unittest
from lru import LRUCache  # code from module you're testing


class LRUTestCase(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        # self.file = open( "blah", "r" )

    def tearDown(self):
        """Call after every test case."""
        # self.file.close()

    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        self.cache = LRUCache(capacity=2)
        self.cache.put(key=2, value=2)
        self.cache.put(key=3, value=3)
        self.cache.put(key=4, value=3)
        self.assertEqual(len(self.cache), 2, "cache size not correct")
        # assert self.cache.size() == 2, "exepected value is 2"

    def testB(self):
        """test case B"""
        self.cache = LRUCache(capacity=2)
        self.cache.put(key=2, value=2)
        self.cache.put(key=3, value=3)
        self.cache.put(key=4, value=3)
        self.assertEqual(self.cache.get(key=2), -1)

    def testC(self):
        """test case C"""
        # assert foo.baz() == "blah", "baz() not returning blah correctly"


if __name__ == "__main__":
    unittest.main()  # run all tests
