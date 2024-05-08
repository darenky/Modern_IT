# Test for stack-based objects
def test_stack_based_objects():
    a = 42
    b = "Hello"
    c = 42
    d = "Hello"

    print("IDs of small integers:")
    print(f"id(a) = {id(a)}")
    print(f"id(c) = {id(c)}")

    print("\nIDs of short strings:")
    print(f"id(b) = {id(b)}")
    print(f"id(d) = {id(d)}")

    # Small integers and short strings are likely to have the same ID,
    # suggesting they are allocated on the stack and reused.

# Test for heap-based objects 
def test_heap_based_objects():
    my_list = [1, 2, 3]
    my_dict = {"a": 1, "b": 2}

    class MyClass:
        pass

    obj = MyClass()

    print("\nIDs of heap-based objects:")
    print(f"id(my_list) = {id(my_list)}")
    print(f"id(my_dict) = {id(my_dict)}")
    print(f"id(obj) = {id(obj)}")

    # Create new instances to observe different IDs
    new_list = [1, 2, 3]
    new_dict = {"a": 1, "b": 2}
    new_obj = MyClass()

    print("\nIDs of new instances:")
    print(f"id(new_list) = {id(new_list)}")
    print(f"id(new_dict) = {id(new_dict)}")
    print(f"id(new_obj) = {id(new_obj)}")

    # Heap-based objects are likely to have different IDs across instances,
    # suggesting they are allocated on the heap.


test_stack_based_objects()
test_heap_based_objects()
