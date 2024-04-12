import unittest
from 2222 import main
from aa import convert_units

class Test_Unit_Convertor(unittest.TestCase):

    def test_invalid_units(self):
        with self.assertRaises(ValueError):
            convert_units(1, "invalid", "m")
        with self.assertRaises(ValueError):
            convert_units(1, "m", "invalid")

    def test_convert_units(self):

        self.assertEqual(convert_units(10, 'cm', 'm'), 0.1)
        self.assertEqual(convert_units(2.5, 'km', 'm'), 2500)
        self.assertEqual(convert_units(5, 'mi', 'km'), 8.04672)
    
    def test_value(self):

        # with self.assertRaisesRegex(ValueError, "Value must be non-negative"):
        #     convert_units(-1, "m", "cm")

        with self.assertRaisesRegex(ValueError, "Value must be numeric"): #or typerror??
            convert_units("ssd", "mm", "cm")
        

    def test_empty_input(self):

        with self.assertRaises(ValueError):
            convert_units("", "m", "m")
        
        with self.assertRaises(ValueError):
            convert_units("1", "", "m")
        
        with self.assertRaises(ValueError):
            convert_units("1", "m", "")



if __name__ == '__main__':
    unittest.main()

    

    
   