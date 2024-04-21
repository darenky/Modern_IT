import unittest
from sorting_strategy import Context, FIFOSortStrategy, FILOSortStrategy, BubbleSortStrategy, QuickSortStrategy

class TestSorting(unittest.TestCase):
    def test_FIFO_strategy(self):
        context = Context(FIFOSortStrategy())
        result = context.strategy.do_algorithm([5, 2, 8, 3, 1])
        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_FILO_strategy(self):
        context = Context(FILOSortStrategy())
        result = context.strategy.do_algorithm([5, 2, 8, 3, 1])
        self.assertEqual(list(result), [8, 5, 3, 2, 1])

    def test_bubble_sort_strategy(self):
        context = Context(BubbleSortStrategy())
        result = context.strategy.do_algorithm([5, 2, 8, 3, 1])
        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_quick_sort_strategy(self):
        context = Context(QuickSortStrategy())
        result = context.strategy.do_algorithm([5, 2, 8, 3, 1])
        self.assertEqual(result, [1, 2, 3, 5, 8])

if __name__ == '__main__':
    unittest.main(verbosity=2)


