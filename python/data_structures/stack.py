# stack.py

class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self.stack = []

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def push(self, item):
        """Pushes an item onto the stack."""
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Removes and returns the top item of the stack. Returns None if the stack is empty."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        """Returns the top item of the stack without removing it. Returns None if the stack is empty."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        """Displays all elements in the stack."""
        print("Stack (top to bottom):", " -> ".join(map(str, reversed(self.stack))) if not self.is_empty() else "Stack is empty")



# Demonstration of Stack operations
if __name__ == "__main__":
    stack = Stack()
    stack.push(25)
    stack.push(75)
    stack.push(9000)

    print("\nCurrent stack:")
    stack.display()

    print("\nTop element:", stack.peek())

    print("\nPopping the top element:", stack.pop())
    stack.display()

    print("\nIs stack empty?", stack.is_empty())
