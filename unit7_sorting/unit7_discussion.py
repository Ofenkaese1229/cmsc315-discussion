"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy of the original list
    sorted_lst = lst.copy()

    # Go through the list multiple times.
    for i in range(len(sorted_lst) - 1):

        # Compare adjacent values.
        # The largest unsorted value moves to the end (right).
        for j in range(0, len(sorted_lst) - i - 1):

            # Swap the values if they are out of order.
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]

    # Return the sorted copy
    return sorted_lst


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base Case: A list w/ 0 or 1 item is already sorted.
    if len(lst) <= 1:
        return lst

    # Find the middle of the list.
    mid = len(lst) // 2

    # Divide the list into two halves.
    left = lst[:mid]
    right = lst[mid:]

    # Recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves.
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # Create a new list for the sorted values
    sorted_lst = []

    # Keep track of current position in each list.
    i = 0
    j = 0

    # Compare items from each half and add the smaller one.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    # Add any remaining item from left half
    sorted_lst.extend(left[i:])

    # Add any remaining item from the right half
    sorted_lst.extend(right[j:])

    return sorted_lst


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    unsorted_lst = [45, 21, 6, 845, 2, 73, 100]

    print("\nORIGINAL UNSORTED LIST")
    print(unsorted_lst)

    bubble_lst = bubble_sort(unsorted_lst)
    print("\nBUBBLE-SORTED LIST")
    print(bubble_lst)

    merge_lst = merge_sort(unsorted_lst)
    print("\nMERGE-SORTED LIST")
    print(merge_lst)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    second_set = [3, 999, 80, 128, 47, 6, 272]

    print("\nORIGINAL UNSORTED LIST")
    print(second_set)

    bubble_second = bubble_sort(second_set)
    print("\nBUBBLE-SORTED LIST")
    print(bubble_second)

    merge_second = merge_sort(second_set)
    print("\nMERGE-SORTED LIST")
    print(merge_second)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print("\nEDGE CASE 1: EMPTY LIST")
    print("-----------------------------")

    empty_list = []
    print("EMPTY LIST")
    print(empty_list)

    bubble_empty = bubble_sort(empty_list)
    print("\nBUBBLE-SORTED LIST")
    print(bubble_empty)

    merge_empty = merge_sort(empty_list)
    print("\nMERGE-SORTED LIST")
    print(merge_empty)

    print("\nEDGE CASE 2: DUPLICATE VALUES")
    print("-----------------------------")

    duplicate_lst = [1, 56, 111, 1, 8, 56, 111]
    print("LIST WITH DUPLICATE VALUES")
    print(duplicate_lst)

    bubble_duplicate = bubble_sort(duplicate_lst)
    print("\nBUBBLE-SORTED LIST")
    print(bubble_duplicate)

    merge_duplicate = merge_sort(duplicate_lst)
    print("\nMERGE-SORTED LIST")
    print(merge_duplicate)


if __name__ == "__main__":
    main()