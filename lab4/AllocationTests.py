import unittest

'''  In Python, you can't directly and definitively determine whether an object
 is stored on the stack or the heap. The language's memory management abstractions 
 make it challenging to investigate memory allocation in the same way as in 
 lower-level languages like C, C++, etc '''

class TestObjects(unittest.TestCase):

    # Test for stack-based objects
    def test_stack_based_objects(self):
        a = 42
        b = "Hello"
        c = 42
        d = "Hello"

        self.assertEqual(id(a), id(c))
        self.assertEqual(id(b), id(d))
        # Small integers and short strings are likely to have the same ID,
        # suggesting they are allocated on the stack and reused

    # Test for heap-based objects 
    def test_heap_based_objects(self):
        my_list = [1, 2, 3]
        my_dict = {"a": 1, "b": 2}

        class MyClass:
            pass

        obj = MyClass()

        self.assertNotEqual(id(my_list), id(my_dict))
        self.assertNotEqual(id(my_list), id(obj))
        self.assertNotEqual(id(my_dict), id(obj))
        # Heap-based objects are likely to have different IDs across instances,
        # suggesting they are allocated on the heap

if __name__ == "__main__":
    unittest.main()
