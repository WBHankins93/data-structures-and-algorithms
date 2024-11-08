# linked_list.py

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_by_value(self, value):
        """Deletes the first node with the given value."""
        if not self.head:
            return "List is empty"

        # If the node to be deleted is the head
        if self.head.data == value:
            self.head = self.head.next
            return

        # Search for the node to delete
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        # If the node was found, unlink it
        if current.next:
            current.next = current.next.next
        else:
            return "Value not found in the list"

    def search(self, value):
        """Searches for a node with the given value."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        """Displays the entire list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


        

# Demonstration of LinkedList operations
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    print("Linked List after insertions:")
    linked_list.display()

    print("\nDeleting value 20:")
    linked_list.delete_by_value(20)
    linked_list.display()

    print("\nSearching for value 10:", linked_list.search(10))
    print("Searching for value 20:", linked_list.search(20))
