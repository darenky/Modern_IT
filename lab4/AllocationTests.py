import unittest
import sys

class TestMemoryAllocation(unittest.TestCase):
    def test_created_on_stack_int(self):  # Heap delta>0
        before_int_allocation = sys.getsizeof(int())
        int_obj = 100
        after_int_allocation = sys.getsizeof(int_obj)  
        int_delta = after_int_allocation - before_int_allocation
        self.assertGreater(int_delta, 0)
 
    def test_created_on_stack_float(self):  # Stack delta=0
        before_float_allocation = sys.getsizeof(int())
        float_obj = 21.9
        after_float_allocation = sys.getsizeof(float_obj)  
        float_delta = after_float_allocation - before_float_allocation
        self.assertEqual(float_delta, 0)

    def test_created_on_heap_list(self): # Heap 
        before_list_allocation = sys.getsizeof([])
        list_obj = [1, 2, 3]
        after_list_allocation = sys.getsizeof(list_obj)  
        list_delta = after_list_allocation - before_list_allocation
        self.assertGreater(list_delta, 0)

    def test_created_on_heap_str(self): # Heap 
        before_str_allocation = sys.getsizeof(str())
        str_obj = "Hello, world!"
        after_str_allocation = sys.getsizeof(str_obj) 
        str_delta = after_str_allocation - before_str_allocation
        self.assertGreater(str_delta, 0)

if __name__ == '__main__':
    unittest.main()


