import unittest
import dumb_code

#v l

class TestTime(unittest.TestCase):

    def test_time(self):
        self.assertEqual(dumb_code.time(3, 12), 4)
        self.assertEqual(dumb_code.time(-3, 12), )
        self.assertEqual(dumb_code.time(3, -12), )
        self.assertEqual(dumb_code.time(-3, -12), )
        


if __name__ == '__main__':
    unittest.main()