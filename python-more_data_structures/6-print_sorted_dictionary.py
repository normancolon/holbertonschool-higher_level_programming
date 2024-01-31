#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Iterate through sorted keys
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
