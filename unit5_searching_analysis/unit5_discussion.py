"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # I added steps and execution time to better show the difference between
    # the two algorithms. Linear search checks items one by one, while binary
    # search cuts the search area in half each time, making it much faster
    # on large sorted datasets.
    steps = 0

    for index in range(len(lst)):
        steps += 1

        # Linear search may check every item, so its time complexity is O(n).
        if lst[index] == target:
            return index, steps
    return -1, steps


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst)-1
    steps = 0

    while low <= high:
        steps += 1

        # Binary search cuts the search space in half each iteration,
        # giving it a time complexity of O(log n).
        mid = (low+high)//2

        if lst[mid] == target:
            return mid, steps
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.\n")

    small_data = [10, 20, 30, 40, 50, 60]

    value_exist = 40
    value_absent = 25

    print(small_data)

    # Search for a value that exists
    idx_linear, linear_steps = linear_search(small_data, value_exist)
    idx_binary, binary_steps = binary_search(small_data, value_exist)

    print(f"\nSearch for {value_exist}: ")
    print(f"\tLinear search -> index: {idx_linear}, steps: {linear_steps}")
    print(f"\tBinary search -> index: {idx_binary}, steps: {binary_steps}")

    # Both searches find the value because 40 is in the list.
    # Binary search uses fewer steps because it eliminates half of the list each time.

    # Search for a value that does not exist
    idx_linear, linear_steps = linear_search(small_data, value_absent)
    idx_binary, binary_steps = binary_search(small_data, value_absent)

    print(f"\nSearch for {value_absent}: ")
    print(f"\tLinear search -> index: {idx_linear}, steps: {linear_steps}")
    print(f"\tBinary search -> index: {idx_binary}, steps: {binary_steps}")

    # Both searches return -1 because 25 is not in the list.
    # Binary search still uses fewer steps because the list is sorted.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    large_data = list(range(1000000))
    target_value = 999999

    # Linear search
    start_time = time.perf_counter()
    lin_search, lin_steps = linear_search(large_data, target_value)
    end_time = time.perf_counter()
    lin_time = end_time - start_time

    # Binary search
    start_time = time.perf_counter()
    bin_search, bin_steps = binary_search(large_data, target_value)
    end_time = time.perf_counter()
    bin_time = end_time - start_time

    print(f"\nList length: {len(large_data)}")
    print(f"Target value: {target_value}")

    print(f"\nLinear search found the target at index {lin_search}.")
    print(f"Linear search steps: {lin_steps}")
    print(f"Linear search time: {lin_time:.4f} seconds.")

    print(f"\nBinary search found the target at index {bin_search}.")
    print(f"Binary search steps: {bin_steps}")
    print(f"Binary search time: {bin_time:.8f} seconds")

    # Linear search checks each item until it finds the target, so it takes
    # 1,000,000 steps in this worst-case example.
    # Binary search cuts the search area in half each time, so it only takes about 20 steps.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Empty list
    empty_lst = []

    print("\nEDGE CASE 1: EMPTY LIST")
    print(empty_lst)

    linear_result, _ = linear_search(empty_lst, 2)
    binary_result, _ = binary_search(empty_lst, 2)

    print(f"\nLinear search on []: {linear_result}")
    print(f"Binary search on []: {binary_result}")

    # Both searches return -1 because the list is empty and the target is not found.

    # Edge Case 2: Value at first position
    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("\nEDGE CASE 2: VALUE AT FIRST POSITION")
    print(lst)

    # Linear search
    start_time = time.perf_counter()
    linear_result, linear_steps = linear_search(lst, 10)
    end_time = time.perf_counter()
    linear_time = end_time - start_time

    print(f"\nLinear search for 10: index {linear_result}")
    print(f"Linear search steps: {linear_steps}")
    print(f"Linear search time: {linear_time:.8f} seconds.")

    # Binary search
    start_time = time.perf_counter()
    binary_result, binary_steps = binary_search(lst, 10)
    end_time = time.perf_counter()
    binary_time = end_time - start_time

    print(f"\nBinary search for 10: index {binary_result}")
    print(f"Binary search steps: {binary_steps}")
    print(f"Binary search time: {binary_time:.8f} seconds.")

    # Linear search finds the first value immediately because it starts at index 0.
    # Binary search still works because the list is sorted.

    # Edge Case 3: Unsorted list
    unsorted_lst = [8, 3, 10, 1, 6, 14, 4]
    print("\nEDGE CASE 3: UNSORTED LIST")

    print(unsorted_lst)

    linear_result, linear_steps = linear_search(unsorted_lst, 3)

    print(f"\nLinear search for 3: index {linear_result}")
    print(f"Linear search steps: {linear_steps}")

    binary_result, binary_steps = binary_search(unsorted_lst, 3)

    print(f"\nBinary search for 3: index {binary_result}")
    print(f"Binary search steps: {binary_steps}")

    # Binary search assumes the list is sorted.
    # Therefore, the result on an unsorted list is unreliable.

if __name__ == "__main__":
    main()