"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

# Parent class
class ParentClass:
    # Class variable
    institute = "University of Maryland"

    # Constructor
    def __init__(self, name, age):

        # Instance variables
        self.name = name
        self.age = age

    # Display method
    def display_info(self):
        return f"{self.name}, Age: {self.age}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

# Child class (inherits from ParentClass)
class ChildClass(ParentClass):
    # New class variable
    grade_level = "Senior"

    # Student-created extension:
    # Class variable shared by ALL ChildClass instances that tracks
    # how many total enrollments have happened across every student.
    total_enrollments = 0

    def __init__(self, name, age, studentID):
        # Inheritance
        super().__init__(name, age)

        # New instance variables
        self.studentID = studentID
        self.enrolled_classes = []

    # New method
    def enroll(self, class_name):
        self.enrolled_classes.append(class_name)
        ChildClass.total_enrollments += 1
        return f"\t{self.name} enrolled in {class_name}."

    # Override parent method
    def display_info(self):
        return (f"\t{super().display_info()}, ID: {self.studentID}, "
                f"Classes: {self.enrolled_classes}")

    # Student-created extension:
    # Removes a class from the student's enrolled list, demonstrating
    # another method that mutates instance-level nested data.
    def graduate(self, class_name):
        if class_name in self.enrolled_classes:
            self.enrolled_classes.remove(class_name)
            return f"\t{self.name} completed and dropped {class_name}."
        return f"\t{self.name} was not enrolled in {class_name}."

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    s1 = ChildClass("James Watson", 26, "UMGC1234")
    s2 = ChildClass("Angie Taylor", 22, "UMGC5678")

    print(f"\n\tClass variable accessed through class: {ChildClass.grade_level}")

    print(f"\tClass variable accessed through object: {s1.grade_level}")

    s1.GPA = 3.2

    print(f"\n\ts1.__dict__ = {s1.__dict__}")
    print(f"\ts2.__dict__ = {s2.__dict__}")

    print(
        f"\n\tChildClass.__dict__ includes: "
        f"grade_level = {ChildClass.__dict__['grade_level']}"
    )

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass("Bob Smith", 29, "UMGC2468")
    original.enroll("MATH 150")
    original.enroll("HISTORY 215")

    # Shallow copy:
    # The object is copied, but the nested enrolled_classes list
    # is still shared between the original and shallow copy.
    shallow_copy = copy(original)

    # Deep copy:
    # The object and its nested enrolled_classes list are
    # copied independently.
    deep_copy = deepcopy(original)

    original.enroll("ART 115")
    original.name = "Bob Smith (Updated)"

    print(f"\n\tOriginal: {original.name}, {original.enrolled_classes}")
    # Shallow copy shares the list, so it sees "ART 115" too
    print(f"\tShallow: {shallow_copy.name}, {shallow_copy.enrolled_classes}")
    # Deep copy has its own list, so it's unaffected
    print(f"\tDeep: {deep_copy.name}, {deep_copy.enrolled_classes}")

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("\n=== Unit 1 OOP Assignment ===")

    person = ParentClass("Lea Port", 32)
    print(f"\n\t{person.display_info()}")

    student = ChildClass("Lucia Mendez", 19, "UMGC1357")

    print(student.display_info())

    print(student.enroll("CMSC 315"))

    demonstrate_namespaces()
    demonstrate_copying()

    # Student-created extension demonstration
    print("\n=== Student Extension: Enrollment Tracking & Graduation ===")
    print(f"\n\tTotal enrollments across all students so far: {ChildClass.total_enrollments}")
    print(student.graduate("CMSC 315"))
    print(f"\t{student.name}'s classes after graduating: {student.enrolled_classes}")

if __name__ == "__main__":
    main()