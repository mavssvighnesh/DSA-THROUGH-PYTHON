from itertools import combinations

def generate_combinations(lst, n):
    return list(combinations(lst, n))

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 2
combinations_of_n = generate_combinations(original_list, n)

# Print the combinations
for combo in combinations_of_n:
    print(combo)
