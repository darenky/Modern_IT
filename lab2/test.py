import unittest
from unit_convertor import convert_units

class Test_Unit_Convertor(unittest.TestCase):

    def test_invalid_units(self):

        with self.assertRaisesRegex(ValueError, "Invalid input"):
            convert_units(1, "m", "invalid")

        with self.assertRaisesRegex(ValueError, "Invalid input"):
            convert_units(1, "invalid", "m")

    def test_convert_units(self):

        self.assertEqual(convert_units(10, 'cm', 'm'), 0.1)
        self.assertEqual(convert_units(2.5, 'km', 'm'), 2500)
        self.assertEqual(convert_units(5, 'mi', 'km'), 8.04672)
    
    # def test_value(self):

    #     #with self.assertRaises(ValueError):
    #         #convert_units(-1, "m", "cm")

    #     with self.assertRaisesRegex("Invalid input"): 
    #         convert_units("ssd", "mm", "cm")
    def test_invalid_input(self):
        result = convert_units("invalid_value", "cm", "mm")
        self.assertIsNone(result)

       # self.assertTrue(value_str.isdigit())
        
    def test_empty_input(self):

        with self.assertRaises(ValueError):
            convert_units("", "m", "m")
        
        with self.assertRaises(ValueError):
            convert_units("1", "", "m")
        
        with self.assertRaises(ValueError):
            convert_units("1", "m", "")


if __name__ == '__main__':
    unittest.main(verbosity=2)

    

    
   