# Data Structures in Python

This folder contains Python implementations of fundamental data structures. Each data structure has its own Python file with code examples and functions to interact with the structure.

## Available Data Structures

### 1. Array

An **array** is a data structure that stores elements of the same type in contiguous memory locations. Arrays allow fast access to elements via an index, making them efficient for read and write operations.

## Array Operations

The `array.py` file demonstrates the following operations:

1. **Access** - Retrieve an element at a specific index.
2. **Modify** - Update an element at a specific index.
3. **Append** - Add an element to the end of the array.
4. **Insert** - Add an element at a specific index.
5. **Remove** - Remove the first occurrence of an element by value.
6. **Pop** - Remove an element at a specific index.

Each function in `array.py` is self-contained and can be called independently to perform the respective operation.

To run the examples, execute:
python array.py


### 2. Linked List

A **linked list** is a linear data structure where elements, called nodes, are linked together using pointers. Each node contains data and a reference (or link) to the next node in the sequence.

#### Linked List Operations

The `linked_list.py` file demonstrates the following operations:

1. **Insert at Beginning** - Adds a new node at the start of the list.
2. **Insert at End** - Adds a new node at the end of the list.
3. **Delete by Value** - Removes the first node with a specified value.
4. **Search** - Checks if a specific value is present in the list.
5. **Display** - Prints all elements in the list.

To run the examples, execute:
python3 linked_list.py

### 3. Stack
A **stack** is a linear data structure that follows the Last-In-First-Out (LIFO) principle. The most recent element added to the stack is the first one to be removed.

- **File**: [`stack.py`](stack.py)
- **Operations**: Push, pop, and peek elements.
- **Example Usage**: (Will add once `stack.py` is implemented.)

### 4. Queue
A **queue** is a linear data structure that follows the First-In-First-Out (FIFO) principle. The first element added to the queue is the first one to be removed.

- **File**: [`queue.py`](queue.py)
- **Operations**: Enqueue and dequeue elements.
- **Example Usage**: (Will add once `queue.py` is implemented.)

### 5. Set
A **set** is an unordered collection of unique elements. Sets are often used to store items without duplicates and to perform mathematical operations like union, intersection, and difference.

- **File**: [`set.py`](set.py)
- **Operations**: Add, remove, and perform set operations.
- **Example Usage**: (Will add once `set.py` is implemented.)

### 6. Map (Dictionary)
A **map** (or dictionary in Python) is a collection of key-value pairs. Each key is unique, and it maps to a specific value. Maps are useful for fast lookups based on unique keys.

- **File**: [`map.py`](map.py)
- **Operations**: Insert, delete, and access values by key.
- **Example Usage**: (Will add once `map.py` is implemented.)

### 7. Binary Tree
A **binary tree** is a tree data structure in which each node has at most two children, referred to as the left and right children. Binary trees are commonly used for searching and sorting.

- **File**: [`binary_tree.py`](binary_tree.py)
- **Operations**: Insert, delete, and traverse nodes (inorder, preorder, and postorder traversal).
- **Example Usage**: (Will add once `binary_tree.py` is implemented.)

### 8. Heap
A **heap** is a special type of binary tree that satisfies the heap property. In a max heap, each parent node is greater than or equal to its child nodes, and in a min heap, each parent node is less than or equal to its child nodes.

- **File**: [`heap.py`](heap.py)
- **Operations**: Insert, delete, and access minimum/maximum elements.
- **Example Usage**: (Will add once `heap.py` is implemented.)

### 9. Graph
A **graph** is a collection of nodes (vertices) and edges connecting them. Graphs can be used to represent various real-world connections, such as social networks, road maps, etc.

- **File**: [`graph.py`](graph.py)
- **Operations**: Add/remove vertices and edges, perform graph traversals (BFS, DFS).
- **Example Usage**: (Will add once `graph.py` is implemented.)

### 10. Trie
A **trie** (prefix tree) is a specialized tree used for storing strings. It’s commonly used for autocomplete and spell-checking applications.

- **File**: [`trie.py`](trie.py)
- **Operations**: Insert, search, and delete words.
- **Example Usage**: (Will add once `trie.py` is implemented.)

---

## Usage

To run any of the data structure examples, navigate to the relevant Python file and run:
python3 <file_name>.py