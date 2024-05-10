import unittest
import ctypes
import sys

class TestMemoryAllocation(unittest.TestCase):
    def test_integer_allocation(self):
        # Get the address of an integer
        x = 42
        address = id(x)
        
        # Use ctypes to determine whether the address belongs to the stack or heap
        stack_bottom = id(ctypes.c_long())
        stack_top = stack_bottom - sys.getsizeof(int()) * 10**6
        on_stack = stack_top <= address <= stack_bottom
        
        self.assertTrue(on_stack, "Integer should be allocated on the stack")

    def test_list_allocation(self):
        # Get the address of a list
        my_list = [1, 2, 3]
        address = id(my_list)
        
        # Use ctypes to determine whether the address belongs to the stack or heap
        stack_bottom = id(ctypes.c_long())
        stack_top = stack_bottom - sys.getsizeof(list()) * 10**6
        on_stack = stack_top <= address <= stack_bottom
        
        self.assertFalse(on_stack, "List should be allocated on the heap")

    def test_string_allocation(self):
        # Get the address of a string
        my_string = "Hello, world!"
        address = id(my_string)
        
        # Use ctypes to determine whether the address belongs to the stack or heap
        stack_bottom = id(ctypes.c_long())
        stack_top = stack_bottom - sys.getsizeof(str()) * 10**6
        on_stack = stack_top <= address <= stack_bottom
        
        self.assertFalse(on_stack, "String should be allocated on the heap")

if __name__ == '__main__':
    unittest.main()
