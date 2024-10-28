class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # The maximum number of items in the queue
        self.queue = [None] * capacity  # Initialize the queue with None values
        self.front = -1  # Points to the front element of the queue
        self.rear = -1   # Points to the rear element of the queue

    def is_empty(self):
        # Check if the queue is empty
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        
        # If the queue is initially empty
        if self.front == -1:
            self.front = 0
            
        # Move the rear pointer in a circular manner
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        
        # Get the front element to return
        item = self.queue[self.front]
        
        # Check if we are removing the last element
        if self.front == self.rear:
            # Reset the queue since it will be empty after this dequeue
            self.front = -1
            self.rear = -1
        else:
            # Move the front pointer in a circular manner
            self.front = (self.front + 1) % self.capacity

        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        
        print("Queue elements:", end=" ")
        
        # Print the elements in the circular queue from front to rear
        index = self.front
        while index != self.rear:
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
        print(self.queue[self.rear])  # Print the last element (rear element)
        
    def size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - (self.front - self.rear - 1)

# Testing the CircularQueue
cq = CircularQueue(5)  # Initialize a circular queue with capacity 5
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()            # Expected output: 1 2 3 4 5 (Queue is full)
cq.dequeue()            # Removes the first element
cq.display()            # Expected output: 2 3 4 5
cq.enqueue(6)           # Enqueues 6 to the circular queue
cq.display()            # Expected output: 2 3 4 5 6
