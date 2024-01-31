#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()  # Ensures a new line at the end
    return count

# Test the function with different scenarios
if __name__ == "__main__":
    safe_print_list = __import__('0-safe_print_list').safe_print_list

    # Test cases as per your requirement
    test_cases = [
        ([1, 2, 3, 4], len([1, 2, 3, 4])),
        ([1, 2, 3, 4], len([1, 2, 3, 4]) - 2),
        ([1, 2, 3, 4], 0),
        ([], 0),
        ([1, 2, 3, 4], len([1, 2, 3, 4]) + 1),
        ([1, 2, 3, 4], len([1, 2, 3, 4]) + 10)
    ]

    for my_list, x in test_cases:
        nb_print = safe_print_list(my_list, x)
        print("nb_print: {:d}".format(nb_print))
