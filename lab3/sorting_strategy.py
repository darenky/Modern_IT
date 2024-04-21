from __future__ import annotations
from abc import ABC, abstractmethod  
from typing import List


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data: List) -> List:
        pass


class FIFOSortStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class FILOSortStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


class BubbleSortStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSortStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.do_algorithm(left) + middle + self.do_algorithm(right)


if __name__ == "__main__":

    context = Context(FIFOSortStrategy())
    print("Client: Strategy is set to FIFO sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to FILO sorting.")
    context.strategy = FILOSortStrategy()
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to Bubble Sort.")
    context.strategy = BubbleSortStrategy()
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to Quick Sort.")
    context.strategy = QuickSortStrategy()
    context.do_some_business_logic()
