import sys
import gc
import unittest

def get_memory_usage(): #get current memory usage
    gc.collect()
    return sys.getsizeof(0)

class TestMemoryAllocation(unittest.TestCase):
    def test_int_storage(self):
        self.check_storage_location(1, "Stack")

    def test_float_storage(self):
        self.check_storage_location(1.0, "Stack")

    def test_bool_storage(self):
        self.check_storage_location(True, "Stack")

    def test_string_storage(self):
        self.check_storage_location("string", "Stack")

    def test_list_storage(self):
        self.check_storage_location([], "Stack")

    def test_tuple_storage(self):
        self.check_storage_location((), "Stack")

    def test_dict_storage(self):
        self.check_storage_location({}, "Stack")

    def check_storage_location(self, value_type, expected_location):

        initial_memory_usage = get_memory_usage()
        obj = value_type
        final_memory_usage = get_memory_usage()
        delta = final_memory_usage - initial_memory_usage

        if delta == 0:
            storage_location = "Stack"
        else:
            storage_location = "Heap"

        self.assertEqual(storage_location, expected_location, f"Value type {type(obj)} should be stored on the {expected_location}")

if __name__ == '__main__':
    unittest.main()
