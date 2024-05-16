# потрібен такий тест:
# 1) створюємо великий об'єкт та зануляємо на нього посилання
# 2) міряємо хіп (h1)
# 3) викликаємо збірку сміття
# 4) міряємо хіп (h2)
# 5) стверджуємо, що h2 < h1 (тобто gc видалив той великий об'єкт і пам'ять звільнилася)

import gc
import unittest
import sys

class TestGarbageCollection(unittest.TestCase):
    def test_garbage_collection(self):
        # 1) створюємо великий об'єкт та зануляємо на нього посилання
        large_object = bytearray(1024 * 1024 * 100)  # 100 MB
        del large_object

        # 2) міряємо хіп (h1)
        h1 = sys.getsizeof(gc.get_objects())

        # 3) викликаємо збірку сміття
        gc.collect()

        # 4) міряємо хіп (h2)
        h2 = sys.getsizeof(gc.get_objects())

        # 5) стверджуємо, що h2 < h1 (тобто gc видалив той великий об'єкт і пам'ять звільнилася)
        self.assertLess(h2, h1)

if __name__ == '__main__':
    unittest.main()