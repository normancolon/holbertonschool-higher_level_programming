# This script prints all possible different combinations of two digits
print(", ".join(f"{i}{j}" for i in range(10) for j in range(i + 1, 10)))