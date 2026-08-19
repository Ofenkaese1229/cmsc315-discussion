"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Adds the value to the top of the stack. Since removals also
        # happen from the top, the most recent push is always removed first (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Removes and returns the top value of the stack. If the stack
        # is empty, returns a message instead of raising an error.
        if self.is_empty():
            return "Cannot pop from an empty stack."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Returns the top value without removing it, leaving the stack
        # unchanged. Useful for checking what's next without altering state.
        if self.is_empty():
            return "Cannot peek from an empty stack."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Checks whether the stack has any values. Returns True if it's
        # empty, which helps other methods avoid invalid operations.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Adds the value to the back of the queue. Since removals happen
        # from the front, the first value added is always removed first (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Removes and returns the front value of the queue. If the queue
        # is empty, returns a message instead of raising an error.
        if self.is_empty():
            return "Cannot dequeue from an empty queue."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Returns the front value without removing it, leaving the queue
        # unchanged. Useful for checking what's next without altering state.
        if self.is_empty():
            return "Cannot check front when queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Checks whether the queue has any values. Returns True if it's
        # empty, which helps other methods avoid invalid operations.
        if len(self.items) == 0:
            return True
        return False


def main():
    print("\n=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

    stack = Stack()

    # 2. Push four values onto the stack.
    #    A stack uses LIFO because the newest value is placed on top
    #    and will be the first value removed.
    stack.push(1)
    print(f"\nPushed: {stack.peek()} || Stack: {stack.items}")
    stack.push(2)
    print(f"Pushed: {stack.peek()} || Stack: {stack.items}")
    stack.push(3)
    print(f"Pushed: {stack.peek()} || Stack: {stack.items}")
    stack.push(4)
    print(f"Pushed: {stack.peek()} || Stack: {stack.items}")

    # 4. LIFO behavior: the LAST item pushed is the FIRST item popped.
    print("\nDEMONSTRATING LIFO BEHAVIOR:")

    print(f"\nPopped: {stack.pop()} || Stack: {stack.items}")
    print(f"Popped: {stack.pop()} || Stack: {stack.items}")
    print(f"Popped: {stack.pop()} || Stack: {stack.items}")
    print(f"Popped: {stack.pop()} || Stack: {stack.items}")

    # 5. Test what happens when pop() is used on an empty stack.
    print(f"\nEmpty stack pop: {stack.pop()}")

    # Edge Cases:
    # 6. Test what happens when peek() is used on an empty stack.
    #    peek() checks the top value without removing anything.
    print(f"\nEmpty stack peek: {stack.peek()}")

    # 7. Test a stack containing only one item.
    #    After the item is removed, the stack should be empty.
    single_stack = Stack()
    single_stack.push(100)

    print(f"\nSingle-item stack: {single_stack.items}")
    print(f"Removed: {single_stack.pop()}")
    print(f"Stack after pop: {single_stack.items}")
    print(f"Is stack empty: {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

    queue = Queue()

    # 2. Add four values to the back of the queue.
    #    A queue uses FIFO because values are removed from the front
    #    in the same order that they were added.
    queue.enqueue(1)
    print(f"\nEnqueued: {queue.items[-1]} || Queue: {list(queue.items)}")
    queue.enqueue(2)
    print(f"Enqueued: {queue.items[-1]} || Queue: {list(queue.items)}")
    queue.enqueue(3)
    print(f"Enqueued: {queue.items[-1]} || Queue: {list(queue.items)}")
    queue.enqueue(4)
    print(f"Enqueued: {queue.items[-1]} || Queue: {list(queue.items)}")

    # 4. FIFO Behavior: The First item enqueued is the FIRST one dequeued.
    print("\nDEMONSTRATING FIFO BEHAVIOR:")

    print(f"\nDequeued: {queue.dequeue()} || Queue: {list(queue.items)}")
    print(f"Dequeued: {queue.dequeue()} || Queue: {list(queue.items)}")
    print(f"Dequeued: {queue.dequeue()} || Queue: {list(queue.items)}")
    print(f"Dequeued: {queue.dequeue()} || Queue: {list(queue.items)}")

    # 5. Test what happens when dequeue() is used on an empty queue.
    print(f"\nEmpty queue dequeue: {queue.dequeue()}")

    # Edge Cases:
    # 6. Test what happens when front() is used on an empty queue.
    #    front() checks the first value without removing it.
    print(f"\nEmpty queue front: {queue.front()}")

    # 7. Test a queue containing only one item.
    #    After the item is removed, the queue should be empty.
    queue_single = Queue()
    queue_single.enqueue(100)

    print(f"\nSingle-item queue: {list(queue_single.items)}")
    print(f"Removed: {queue_single.dequeue()}")
    print(f"Queue after dequeue: {list(queue_single.items)}")
    print(f"Is queue empty: {queue_single.is_empty()}")


if __name__ == "__main__":
    main()
