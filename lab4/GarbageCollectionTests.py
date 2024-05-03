import gc

class MyObject:
    def __init__(self, name):
        self.name = name
        self.obj_info = f"Object Name: {name}, Object ID: {id(self)}"

    def __del__(self):
        print(f"Object with ID: {id(self)} is being deleted.")

def manual_collect():
    print("Calling garbage collector...")
    collected = gc.collect()
    print(f"Unreachable objects collected: {collected}")
    print("Garbage collection finished.")

def main():
    obj1 = MyObject("Object 1")
    obj2 = MyObject("Object 2")
    obj3 = MyObject("Object 3")

    print(obj1.obj_info)
    print(obj2.obj_info)
    print(obj3.obj_info)

    del obj1
    del obj2

    manual_collect()

    obj4 = MyObject("Object 4")
    obj5 = MyObject("Object 5")
    obj4.obj5 = obj5
    obj5.obj4 = obj4

    manual_collect()

    del obj4
    del obj5

    manual_collect()

if __name__ == "__main__":
    main()
