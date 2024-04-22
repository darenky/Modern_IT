import unittest
from sorting_strategy import Context, FIFOSortStrategy, LIFOSortStrategy, BubbleSortStrategy, QuickSortStrategy

class TestSorting(unittest.TestCase):
    def test_fifo_sort_strategy(self):
        context = Context(FIFOSortStrategy())
        result = context.do_some_business_logic()
        self.assertEqual(result, ["a", "b", "c", "d", "e"])

    def test_lifo_sort_strategy(self):
        context = Context(LIFOSortStrategy())
        result = context.do_some_business_logic()
        self.assertEqual(result, ["e", "d", "c", "b", "a"])

    def test_bubble_sort_strategy(self):
        context = Context(BubbleSortStrategy())
        result = context.do_some_business_logic()
        self.assertEqual(result, ["a", "b", "c", "d", "e"])

    def test_quick_sort_strategy(self):
        context = Context(QuickSortStrategy())
        result = context.do_some_business_logic()
        self.assertEqual(result, ["a", "b", "c", "d", "e"])

if __name__ == '__main__':
    unittest.main()




