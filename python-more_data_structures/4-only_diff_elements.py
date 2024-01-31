def only_diff_elements(set_1, set_2):
    # Return the symmetric difference of set_1 and set_2
    return set_1.symmetric_difference(set_2)

# Test the function
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))

