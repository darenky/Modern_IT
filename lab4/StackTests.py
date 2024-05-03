class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Stack({self.items})"

def test_stack():
    # Test case 1: Test pushing and popping items
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert str(stack) == "Stack([1, 2, 3])"
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert str(stack) == "Stack([1])"

    # Test case 2: Test peeking and length
    stack.push(4)
    stack.push(5)
    assert stack.peek() == 5
    assert len(stack) == 3

    # Test case 3: Test popping from an empty stack
    while not stack.is_empty():
        stack.pop()
    try:
        stack.pop()
        assert False, "Expected IndexError"
    except IndexError:
        pass

    # Test case 4: Test peeking from an empty stack
    try:
        stack.peek()
        assert False, "Expected IndexError"
    except IndexError:
        pass

    print("All test cases passed!")

if __name__ == "__main__":
    test_stack()