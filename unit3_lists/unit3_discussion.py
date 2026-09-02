"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Insert the new value at the specified position.
    # Existing elements at that index and after shift to the right.
    # Inserting near the beginning requires more shifting than at the end
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Verify that the index refers to an existing item
    if 0 <= index < len(lst):
        # Later elements shift left after the item is removed.
        return lst.pop(index)
    # Return None instead of causing an error
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks each item in order.
    for index in range(len(lst)):
        # Return the index when a match is found
        if lst[index] == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================

    # 1. Create a list containing several values.
    numbers = [10, 20, 30, 40]

    # 2. Display the original list.
    print("\nOriginal list: ", numbers)


    # Insert a value at the beginning of the list.
    # All existing elements shift one position to the right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert a value in the middle of the list.
    # Elements after the insertion point shift to the right.
    insert_at(numbers, 3, 15)
    print("After inserting 15 in the middle:", numbers)

    # Insert a value at the end of the list.
    # No existing elements need to be shifted beyond the end position.
    insert_at(numbers, len(numbers), 25)
    print("After inserting 25 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Remove the first item in the list.
    removed = delete_at(numbers, 0)
    print("\nRemoved from beginning: ", removed)
    print("Updated list: ", numbers)

    # Calculate the middle index and remove the item at that position.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("\nRemoved from middle: ", removed)
    print("Updated list: ", numbers)

    # Remove the last item in the list.
    removed = delete_at(numbers, len(numbers)-1)
    print("\nRemoved from end: ", removed)
    print("Updated list: ", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Search for a value that is currently in the list.
    value = 20
    result = search_value(numbers, value)

    if result != -1:
        print(f"\nSearch for {value}: found at index {result}")
    else:
        print(f"\nSearch for {value}: not found")

    # Search for a value that does not exist in the list.
    value = 99
    result = search_value(numbers, value)

    if result != -1:
        print(f"Search for {value}: found at index {result}")
    else:
        print(f"Search for {value}: not found")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Attempt to delete an item using an index outside the list.
    # The function safely returns None instead of causing an error.
    removed = delete_at(numbers, 100)
    print("\nDelete using invalid index 100: ", removed)

    # Search for a value that is not present in the list.
    # The function returns -1 when no match is found.
    result = search_value(numbers, 100)
    print("Search for missing value 100: ", result)

    # Insert a value into an empty list.
    # This demonstrates that insertion works even when the list has no items.
    empty_list = []
    insert_at(empty_list, 0, "First Item")
    print("Insert into empty list:", empty_list)

    # Attempt to delete an item from an empty list.
    # Since no valid index exists, the function returns None.
    another_empty_list = []
    removed = delete_at(another_empty_list, 0)
    print("Delete from empty list:", removed )



if __name__ == "__main__":
    main()