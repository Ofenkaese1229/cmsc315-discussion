# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

This assignment reinforced my understanding of two fundamental data structures: the Stack (LIFO) 
and the Queue (FIFO). I learned how a Python list naturally supports stack behavior, 
since append() and pop() both operate on the same end, giving LIFO order without extra effort. 
For the queue, I used collections.deque instead of a list, which taught me why popleft() is more 
efficient than removing from the front of a list, an important distinction I hadn't previously 
considered.

The main challenge was handling edge cases correctly, like popping from an empty stack or 
dequeuing from an empty queue. My first instinct was to let these raise unhandled exceptions, 
but I realized returning a clear message instead is far more predictable and mirrors how real 
systems handle failure gracefully rather than crashing.

Stacks and queues serve very different purposes in real-world systems despite both managing 
ordered data. Stacks fit situations where the most recent action matters most, like undo 
functionality in a text editor or the call stack that tracks function execution. Queues fit 
situations where fairness and order of arrival matter, like a print job queue or a customer 
support ticket system, where the first request in should be the first one handled. 
Recognizing which structure actually matches a problem's requirements, rather than defaulting 
to whichever is more familiar, is the real skill this assignment reinforced.