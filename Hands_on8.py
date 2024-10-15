

# Quicksort Que 1

import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        # Check if pivot_index is the kth element
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)

    return None

def find_ith_order_statistic(arr, i):
    return quickselect(arr, 0, len(arr) - 1, i - 1)

# Example usage:
arr = [12, 3, 5, 7, 19, 10]
i = 4
ith_smallest = find_ith_order_statistic(arr, i)
print(f"The {i}-th smallest element is: {ith_smallest}")


# Que 2
# Stack implementation

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity  # Fixed-size array
        self.top = -1  # Initially, the stack is empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def size(self):
        return self.top + 1

# Example usage:
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())
print("Stack size:", stack.size())
stack.pop()
print("Stack after pop:", stack.peek())


# Queue Implemenatation

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity  # Fixed-size array
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def front_value(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def queue_size(self):
        return self.size

# Example usage:
queue = Queue(5)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print("Front element:", queue.front_value())
queue.dequeue()
print("Front element after dequeue:", queue.front_value())


# Single Linked List Implementation

class SinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * capacity  # Data array (C-style int)
        self.next = [-1] * capacity  # Next index array
        self.head = -1  # Head pointer
        self.free = 0  # Free list pointer
        for i in range(capacity - 1):
            self.next[i] = i + 1
        self.next[capacity - 1] = -1  # Last element

    def is_empty(self):
        return self.head == -1

    def insert_at_head(self, value):
        if self.free == -1:
            raise OverflowError("List is full")
        new_node = self.free  # Get the first free position
        self.free = self.next[new_node]  # Update the free list pointer
        self.data[new_node] = value
        self.next[new_node] = self.head  # Point new node to the current head
        self.head = new_node  # Update head to new node

    def delete_from_head(self):
        if self.is_empty():
            raise IndexError("List is empty")
        node_to_delete = self.head
        self.head = self.next[node_to_delete]  # Update head to next node
        self.next[node_to_delete] = self.free  # Add deleted node to free list
        self.free = node_to_delete  # Update free list pointer

    def display(self):
        current = self.head
        while current != -1:
            print(self.data[current], end=" -> ")
            current = self.next[current]
        print("None")

# Example usage:
linked_list = SinglyLinkedList(5)
linked_list.insert_at_head(10)
linked_list.insert_at_head(20)
linked_list.insert_at_head(30)
linked_list.display()
linked_list.delete_from_head()
linked_list.display()
