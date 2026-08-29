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
    #
    # Requirements:
    # 1. Create a list containing several values.
    numbers = [10, 20, 30, 40]

    # 2. Display the original list.
    print("\nOriginal list: ", numbers)

    # 3. Test insertion at:

    #    - the beginning
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    #    - the middle
    insert_at(numbers, 3, 15)
    print("After inserting 15 in the middle:", numbers)

    #    - the end
    insert_at(numbers, len(numbers), 25)
    print("After inserting 25 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    # Requirements:
    # 1. Delete an item from:

    #    - the beginning
    removed = delete_at(numbers, 0)
    print("\nRemoved from beginning: ", removed)
    print("Updated list: ", numbers)

    #    - the middle
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("\nRemoved from middle: ", removed)
    print("Updated list: ", numbers)

    #    - the end
    removed = delete_at(numbers, len(numbers)-1)
    print("\nRemoved from end: ", removed)
    print("Updated list: ", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    # Requirements:
    # 1. Search for a value that exists.
    value = 20
    result = search_value(numbers, value)

    if result != -1:
        print(f"\nSearch for {value}: found at index {result}")
    else:
        print(f"\nSearch for {value}: not found")

    # 2. Search for a value that does not exist.
    value = 99
    result = search_value(numbers, value)

    if result != -1:
        print(f"Search for {value}: found at index {result}")
    else:
        print(f"Search for {value}: not found")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    # Example ideas:
    # - Delete using an invalid index
    removed = delete_at(numbers, 100)
    print("\nDelete using invalid index 100: ", removed)
    # - Search for a missing value
    result = search_value(numbers, 100)
    print("Search for missing value 100: ", result)

    # - Insert into an empty list
    empty_list = []
    insert_at(empty_list, 0, "First Item")
    print("Insert into empty list:", empty_list)

    # - Delete from an empty list
    another_empty_list = []
    removed = delete_at(another_empty_list, 0)
    print("Delete from empty list:", removed )
    # - Use comments to explain each edge case.




if __name__ == "__main__":
    main()