d#!/usr/bin/python3
ef number_keys(a_dictionary):
    # Return the number of keys in the dictionary
    return len(a_dictionary.keys())

# Test the function
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
