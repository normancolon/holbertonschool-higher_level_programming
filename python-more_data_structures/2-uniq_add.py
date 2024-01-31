def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates
    unique_numbers = set(my_list)
    # Sum up the unique numbers
    return sum(unique_numbers)

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

