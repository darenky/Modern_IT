import unittest
from unit_convertor import convert_units

class Test_Unit_Convertor(unittest.TestCase):

    def test_invalid_units(self):

        with self.assertRaisesRegex(ValueError, "ONLY mm,cm,m,km,mi ARE ACCEPTED"):
            convert_units(1, "m", "invalid")

        with self.assertRaisesRegex(ValueError, "ONLY mm,cm,m,km,mi ARE ACCEPTED"):
            convert_units(1, "invalid", "m")

    def test_convert_units(self):

        self.assertEqual(convert_units(10, 'cm', 'm'), 0.1)
        self.assertEqual(convert_units(2.5, 'km', 'm'), 2500)
        self.assertEqual(convert_units(5, 'mi', 'km'), 8.04672)
    
    def test_value(self):

        with self.assertRaisesRegex(ValueError,"VALUE MUST BE NON-NEGATIVE NUMERIC"): 
            convert_units("invalid", "mm", "cm")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

    

    
   