import unittest
import dumb_code

class TestTime(unittest.TestCase):

    def test_time(self):
        self.assertEqual(dumb_code.time(3, 12), 4)

        with self.assertRaises(ValueError):
            dumb_code.time(0, 12)
        
        with self.assertRaises(ValueError):
            dumb_code.time(-1, 12)

        with self.assertRaises(ValueError):
            dumb_code.time(1, -12)

        with self.assertRaises(ValueError):
            dumb_code.time(-1, -12)

        
if __name__ == '__main__':
    unittest.main()