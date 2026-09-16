"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Dictionary stores key-value pairs.
    # Keys are hashed internally for fast lookups.
    student_info = {}

    # Add 5 key-value pairs.
    student_info["Name"] = "James Brown"
    student_info["ID"] = 2567945
    student_info["Email"] = "brown.james@school.edu"
    student_info["Major"] = "Chemistry"
    student_info["Grade"] = "Junior"
    # Each key is used to access its associated value.

    # Display the contents of the dictionary.
    print("\nDICTIONARY CONTENT:")
    for key, value in student_info.items():
        print(f"{key:<8} : {value}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Use a key to retrieve its value.
    print(f"\nName     : {student_info.get('Name')}")
    print(f"ID       : {student_info.get('ID')}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("\nDICTIONARY BEFORE UPDATED VALUE:")
    for key, value in student_info.items():
        print(f"{key:<8} : {value}")

    # Existing key: its value is replaced.
    student_info["Name"] = "Peter Parker"

    print("\nDICTIONARY AFTER UPDATED VALUE:")
    for key, value in student_info.items():
        print(f"{key:<8} : {value}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("\nDICTIONARY BEFORE DELETED VALUE:")
    for key, value in student_info.items():
        print(f"{key:<8} : {value}")

    # pop() removes the key and its value.
    student_info.pop("Email")
    student_info.pop("Major")

    print("\nDICTIONARY AFTER DELETED VALUE:")
    for key, value in student_info.items():
        print(f"{key:<8} : {value}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    print("\nEDGE CASE 1: LOOK UP A NON EXISTING KEY")
    # get() returns None if the key is missing.
    missing_value = student_info.get("Phone")

    if missing_value is None:
        print("\tLookup for 'Phone': Key does not exist.")

    print("\nEDGE CASE 2: REMOVING A NON EXISTING KEY")
    # Check if the key exists before removing it.
    if "Phone" in student_info:
        student_info.pop("Phone")
    else:
        print("\tDelete 'Phone': Key does not exist, so nothing was deleted.")

    print("\nEDGE CASE 3: UPDATE A NON EXISTING KEY")
    # Check if the key exists before updating it.
    if "Phone" in student_info:
        student_info["Phone"] = "256-623-0092"
    else:
        print("\tUpdate 'Phone': Key does not exist, so nothing was updated.")

    print("\nEDGE CASE 4: LOOKUP IN AN EMPTY DICTIONARY")
    empty_dictionary = {}

    result = empty_dictionary.get("Name")

    if result is None:
        print("\tThe dictionary is empty, so 'Name' cannot be found.")

if __name__ == "__main__":
    main()