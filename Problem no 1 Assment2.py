def sort_list_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

# Example usage:
original_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_list_by_last_element(original_list)
print(sorted_list)
