# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

This assignment strengthened my understanding of core OOP concepts in Python, 
particularly inheritance, class versus instance namespaces, and the distinction between 
shallow and deep copying. Building a parent and child class showed me how super() lets 
a subclass extend rather than fully replace inherited behavior, while the namespace demo 
clarified how instance attributes stay isolated even when a class variable is shared across objects.

The most challenging part was correctly demonstrating shallow versus deep copy. 
My first attempt didn't clearly show the difference because I mutated an immutable attribute 
(a string) instead of the nested mutable list. Once I mutated the enrolled_classes list 
after copying, the shallow copy correctly reflected the change while the deep copy stayed 
independent, which made the concept concrete rather than theoretical.
Compared to procedural programming, where logic and data are separate and code runs top-down 
through functions, OOP bundles data and behavior together into objects, 
making relationships between entities more explicit.

This structure directly supports maintainability and reusability: 
changes to shared logic happen in one place (the parent class), new features extend existing code
rather than duplicating it, and future development can build on existing classes with far less 
overhead than rewriting procedural functions from scratch.

