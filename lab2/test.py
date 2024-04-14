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


    @patch('sys.stdin', new_callable=io.StringIO) 
    def test_exit_code(self, mock_stdin):
        # Simulate incorrect input
        mock_stdin.write('invalid\n')
        mock_stdin.seek(0)

        # Capture stdout and stderr
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout, \
             patch('sys.stderr', new=io.StringIO()) as mock_stderr:
            # Call the main function with incorrect input
            with self.assertRaises(SystemExit) as cm:
                main()

            # Check for the expected error message
            self.assertEqual(mock_stderr.getvalue(), 'Wrong format\n')
            self.assertEqual(mock_stdout.getvalue(), '')
            self.assertEqual(cm.exception.code, 1)


    @patch('sys.stdin', new_callable=io.StringIO)
    def test_stderr(self, mock_stdin):
        mock_stdin.write('invalid km\n')
        mock_stdin.seek(0)

        with patch('sys.stdout', new=io.StringIO()) as mock_stdout, \
             patch('sys.stderr', new=io.StringIO()) as mock_stderr:
            
            with self.assertRaises(SystemExit) as cm:
                main()

            self.assertRegex(mock_stderr.getvalue(), 'Wrong format\n')
            self.assertEqual(mock_stdout.getvalue(), '')
            self.assertEqual(cm.exception.code, 1)


    def test_stdin_to_unit(self):
        with patch('sys.stdin', new_callable=io.StringIO) as mock_stdin, \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            
            mock_stdin.write('1 m\n')
            mock_stdin.seek(0)

            sys.argv = ['unit_convertor.py', 'cm'] 

            main()

            self.assertEqual(mock_stdout.getvalue(), '100.0\n')  


if __name__ == '__main__':
    unittest.main(verbosity=2)


        


    

    
   