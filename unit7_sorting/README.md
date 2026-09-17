# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

Through this assignment, I developed a hands-on understanding of Bubble Sort (an iterative,
comparison-based algorithm) and Merge Sort (a recursive, divide-and-conquer algorithm).
Implementing Bubble Sort reinforced nested loop iteration and adjacent swapping mechanic s
to move values into order. Building merge_sort() deepened my understanding of recursion,
more specifically, defining base cases, splitting lists into left and right halves
using midpoint calculations, and writing a dedicated merge() helper function to combine
two sorted sub-lists into a final sorted array.

2. What challenges did you encounter, and how did you overcome them?

Both merge_sort() and bubble_sort() were a bit challenging at first, but everything
became much clearer once the underlying logic clicked. For bubble_sort(), the breakthrough
came from visualizing how the outer loop reduces the inner comparison range
(len(sorted_lst) - i - 1) as the largest elements "bubble" to the end. For merge_sort(),
the main hurdle was tracking how recursion unwinds and ensuring the merge() helper
correctly tracked sub-list indices (i and j) before using .extend() to append any
remaining elements. Stepping through the code execution manually helped solidify how
both algorithms process datasets.

3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

bubble_sort() operates at O(n^2) quadratic time complexity with O(1) auxiliary space,
making it efficient for tiny or nearly-sorted datasets where memory is constrained,
but extremely slow as data volume grows. In contrast, merge_sort() guarantees O(n log n)
logarithmic time performance regardless of the initial data order, though it makes
a space tradeoff by requiring O(n) extra memory to allocate recursive sub-lists. 
In real-world applications, bubble_sort() is best reserved for simple educational
examples or low-overhead scripts on small lists, while merge_sort() is the ideal
choice for large-scale production databases and systems where consistent search and
sort speeds outweigh the cost of additional memory usage.