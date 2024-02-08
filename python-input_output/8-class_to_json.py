#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing all serializable attributes of obj.
    """
    return obj.__dict__

# The script below is to demonstrate how to use the `class_to_json` function, as shown in the examples provided.
if __name__ == "__main__":
    # Assuming the existence of 'MyClass' and 'MyClass2' from the provided examples
    MyClass = __import__('8-my_class').MyClass
    # Use the function with an instance of MyClass
    m = MyClass("John")
    m.number = 89
    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    MyClass2 = __import__('8-my_class_2').MyClass
    # Use the function with an instance of MyClass2
    m2 = MyClass2("John")
    m2.win()
    mj2 = class_to_json(m2)
    print(type(mj2))
    print(mj2)
#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing all serializable attributes of obj.
    """
    return obj.__dict__

# The script below is to demonstrate how to use the `class_to_json` function, as shown in the examples provided.
if __name__ == "__main__":
    # Assuming the existence of 'MyClass' and 'MyClass2' from the provided examples
    MyClass = __import__('8-my_class').MyClass
    # Use the function with an instance of MyClass
    m = MyClass("John")
    m.number = 89
    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    MyClass2 = __import__('8-my_class_2').MyClass
    # Use the function with an instance of MyClass2
    m2 = MyClass2("John")
    m2.win()
    mj2 = class_to_json(m2)
    print(type(mj2))
    print(mj2)
