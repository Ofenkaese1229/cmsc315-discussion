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

Working through this assignment really solidified my understanding of core OOP concepts in Python,
especially inheritance, the difference between class and instance namespaces, and shallow versus 
deep copying. Building out a parent and child class made it click for me how super() lets a subclass
build on top of inherited behavior instead of just overwriting it entirely. 

The namespace exercise was also useful for seeing how instance attributes stay separate for each 
object, even when a class variable is being shared across all of them.

The part that gave me the most trouble was actually demonstrating shallow versus deep copy 
in a way that showed a real difference. My first attempt fell flat because I was mutating an 
immutable attribute, a string, instead of the nested list. Once I switched to mutating 
enrolled_classes after copying, everything made sense: the shallow copy picked up the change, 
since it was still pointing to the same list, while the deep copy stayed completely independent. 

Thinking about this compared to procedural programming, where data and logic live separately and 
everything runs top-down through functions, OOP feels like a different way of organizing a 
problem entirely. Bundling data and behavior together into objects makes the relationships between
different parts of the program much more explicit and easier to reason about.

That structure ends up paying off in terms of maintainability and reusability, too. Since shared 
logic lives in the parent class, updates only need to happen once, and new functionality can 
extend what's already there instead of duplicating it. That means future development builds on 
existing classes rather than requiring a rewrite from scratch, which is a huge time saver 
compared to procedural code.

