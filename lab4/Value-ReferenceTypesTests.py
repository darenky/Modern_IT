import unittest
import sys

class TestValueReferenceTypes(unittest.TestCase):

    def test_pass_by_value_number(self):
        def modify_value(x):
            x += 1
            return x

        original_value = 5
        modified_value = modify_value(original_value)

        self.assertEqual(original_value, 5)  # Check that original value is not modified
        self.assertEqual(modified_value, 6)  # Check that modified value is modified

    def test_created_on_stack(self):
        before_allocation = sys.getsizeof([])  
        obj_ = 42  
        after_allocation = sys.getsizeof([])
        delta = after_allocation - before_allocation
        self.assertEqual(delta, 0)

    def test_pass_by_value_string(self):
        def modify_string(s):
            s += " world"
            return s

        original_string = "hello"
        modified_string = modify_string(original_string)

        self.assertEqual(original_string, "hello")  
        self.assertEqual(modified_string, "hello world")   

    def test_pass_by_value_bool(self):
        def negate_boolean(b):
            b = not b
            return b

        original_bool = True
        modified_bool = negate_boolean(original_bool)

        self.assertEqual(original_bool, True)   
        self.assertEqual(modified_bool, False)

    def test_pass_by_reference_tuple(self):
        def modify_tuple(t):
            t += (4,)
            return t

        original_tuple = (1, 2, 3)
        modified_tuple = modify_tuple(original_tuple)

        self.assertEqual(original_tuple, (1, 2, 3))  
        self.assertEqual(modified_tuple, (1, 2, 3, 4))

    def test_pass_by_reference_list(self):
        def modify_list(lst):
            lst.append(4)
            return lst

        original_list = [1, 2, 3]
        modified_list = modify_list(original_list)

        self.assertEqual(original_list, [1, 2, 3, 4])
        self.assertEqual(modified_list, [1, 2, 3, 4])   

    def test_pass_by_reference_dictionary(self):
        def modify_dict(d):
            d["key"] = "value"
            return d

        original_dict = {"a": 1, "b": 2}
        modified_dict = modify_dict(original_dict)

        self.assertEqual(original_dict, {"a": 1, "b": 2, "key": "value"})  
        self.assertEqual(modified_dict, {"a": 1, "b": 2, "key": "value"})   

    def test_pass_by_reference_set(self):
        def modify_set(s):
            s.add(4)
            return s

        original_set = {1, 2, 3}
        modified_set = modify_set(original_set)

        self.assertEqual(original_set, {1, 2, 3, 4}) 
        self.assertEqual(modified_set, {1, 2, 3, 4})   

if __name__ == '__main__':
    unittest.main()