import gc
import unittest
import psutil

# RSS stands for "Resident Set Size."
# In the context of memory usage, it refers to the portion of a process's memory that is held in RAM (Random Access Memory).
# It includes the memory used by the process's code, data, and shared libraries, but it excludes memory
# that has been swapped out to disk or memory that is shared with other processes.

class TestGarbageCollection(unittest.TestCase):
    def test_garbage_collection(self):
        process = psutil.Process()

        # 1) створюємо великий об'єкт та зануляємо на нього посилання
        large_object = bytearray(1024 * 1024 * 100)  # 100 MB

        # 2) міряємо хіп (h1)
        h1 = process.memory_info().rss 
        del large_object

        # 3) викликаємо збірку сміття
        gc.collect()

        # 4) міряємо хіп (h2)
        h2 = process.memory_info().rss

        # 5) стверджуємо, що h2 < h1 (тобто gc видалив той великий об'єкт і пам'ять звільнилася)
        self.assertLess(h2, h1)

if __name__ == '__main__':
    unittest.main()
