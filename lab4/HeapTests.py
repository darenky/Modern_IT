import heapq

def test_max_heap():
    max_heap = []

    # Test case 1: Insert elements into the max heap
    heapq.heappush(max_heap, -3)
    heapq.heappush(max_heap, -1)
    heapq.heappush(max_heap, -4)
    heapq.heappush(max_heap, -2)
    assert max_heap == [-4, -2, -3, -1]

    # Test case 2: Remove elements from the max heap
    assert -heapq.heappop(max_heap) == 4
    assert -heapq.heappop(max_heap) == 3
    assert -heapq.heappop(max_heap) == 2
    assert -heapq.heappop(max_heap) == 1
    assert len(max_heap) == 0

    # Test case 3: Remove from an empty heap
    try:
        heapq.heappop(max_heap)
        assert False, "Expected IndexError"
    except IndexError:
        pass

    print("Max Heap tests passed!")


def test_min_heap():
    min_heap = []

    # Test case 1: Insert elements into the min heap
    heapq.heappush(min_heap, 3)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 4)
    heapq.heappush(min_heap, 2)

    # Sort the list to ensure the correct order
    min_heap.sort()

    assert min_heap == [1, 2, 3, 4]

    # Test case 2: Remove elements from the min heap
    assert heapq.heappop(min_heap) == 1
    assert heapq.heappop(min_heap) == 2
    assert heapq.heappop(min_heap) == 3
    assert heapq.heappop(min_heap) == 4
    assert len(min_heap) == 0

    # Test case 3: Remove from an empty heap
    try:
        heapq.heappop(min_heap)
        assert False, "Expected IndexError"
    except IndexError:
        pass

    print("Min Heap tests passed!")

if __name__ == "__main__":
    test_max_heap()
    test_min_heap()
