import unittest
from unit_convertor import convert_units
from unittest.mock import patch
from unit_convertor import main
import sys
import io

class Test_Unit_Convertor(unittest.TestCase):

    def test_invalid_units(self):

        with self.assertRaisesRegex(ValueError, "Only mm, cm, m, km, mi are accepted."):
            convert_units(1, "m", "invalid")

        with self.assertRaisesRegex(ValueError, "Only mm, cm, m, km, mi are accepted."):
            convert_units(1, "invalid", "m")

    def test_convert_units(self):

        self.assertEqual(convert_units(10, 'cm', 'm'), 0.1)
        self.assertEqual(convert_units(2.5, 'km', 'm'), 2500)
        self.assertEqual(convert_units(5, 'mi', 'km'), 8.04672)
    
    def test_value(self):

        with self.assertRaisesRegex(ValueError, "Value must be numeric."): 
            convert_units("invalid", "mm", "cm")

    # @patch('sys.exit')
    # def test_invalid_input_format(self, mock_exit):
    #     with patch('sys.stdin', new=io.StringIO('100')):
    #         main()
    #         mock_exit.assert_called_once_with(1)

    # @patch('sys.exit')
    # def test_missing_to_unit(self, mock_exit):
    #     sys.argv = ['unit_convertor.py']
    #     with patch('sys.stdin', new=io.StringIO('100 m')):
    #         main()
    #         mock_exit.assert_called_once_with(1)

    # @patch('sys.exit')
    # def test_valid_input(self, mock_exit):
    #     sys.argv = ['unit_convertor.py', 'cm']
    #     with patch('sys.stdin', new=io.StringIO('100 m')):
    #         main()
    #         mock_exit.assert_not_called()
 
    # def test_exit_code(capsys):
    #     main([1,'m'])
    #     out, err = capsys.readouterr()
    #     assert out == ''
    #     assert err == 'Wrong format'

        
if __name__ == '__main__':
    unittest.main(verbosity=2)

    

    
   