import unittest
import gc
import sys  

class TestGarbageCollector(unittest.TestCase):

    def setUp(self):
        self.large_object = [None] * (10 ** 7)  

    def tearDown(self):
        del self.large_object
        gc.collect()

    def test_collection(self):
        large_object = [None] * (10 ** 7)
        del large_object
        gc.collect()
        self.assertLess(gc.get_count()[0], 10)

    def test_reference_counting(self):
        obj = object()
        initial_refcount = sys.getrefcount(obj)
        another_ref = obj
        self.assertEqual(sys.getrefcount(obj), initial_refcount + 1)
        del another_ref
        self.assertEqual(sys.getrefcount(obj), initial_refcount)

    def test_cycle_detection(self):
        obj1 = {}
        obj2 = {}
        obj1['obj2'] = obj2
        obj2['obj1'] = obj1
        del obj1, obj2
        gc.collect()
        self.assertEqual(gc.get_count()[0], 0)

if __name__ == '__main__':
    unittest.main()