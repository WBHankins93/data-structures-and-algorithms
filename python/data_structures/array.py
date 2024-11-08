# array.py

def display_array(arr):
    """Displays the contents of an array."""
    print("Array:", arr)

def access_element(arr, index):
    """Accesses an element at a specific index."""
    try:
        return arr[index]
    except IndexError:
        return "Index out of bounds"

def modify_element(arr, index, value):
    """Modifies an element at a specific index."""
    try:
        arr[index] = value
        return arr
    except IndexError:
        return "Index out of bounds"

def append_element(arr, value):
    """Appends an element to the end of the array."""
    arr.append(value)
    return arr

def insert_element(arr, index, value):
    """Inserts an element at a specific index."""
    arr.insert(index, value)
    return arr

def remove_element(arr, value):
    """Removes the first occurrence of a specific element."""
    try:
        arr.remove(value)
        return arr
    except ValueError:
        return "Value not found in array"

def pop_element(arr, index):
    """Removes an element at a specific index."""
    try:
        return arr.pop(index)
    except IndexError:
        return "Index out of bounds"
    
    

# Demonstration of array operations
if __name__ == "__main__":
    # Initial array
    arr = [1, 2, 3, 4, 5]
    print("Initial array:")
    display_array(arr)

    # Access element
    print("\nAccess element at index 2:", access_element(arr, 2))

    # Modify element
    print("\nArray after modifying element at index 1 to 10:")
    display_array(modify_element(arr, 1, 10))

    # Append element
    print("\nArray after appending 6:")
    display_array(append_element(arr, 6))

    # Insert element
    print("\nArray after inserting 7 at index 2:")
    display_array(insert_element(arr, 2, 7))

    # Remove element
    print("\nArray after removing element 10:")
    display_array(remove_element(arr, 10))

    # Pop element
    print("\nElement popped at index 2:", pop_element(arr, 2))
    display_array(arr)
