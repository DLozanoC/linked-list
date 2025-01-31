
# Defines a node in the singly linked list
from types import new_class


class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.previous = prev_node #This line because this is a doubly linked list

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
        self.tail = None

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is None:
            return None
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)

        else:
            new_node = Node(value, self.head)
            self.head.previous = new_node
            self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current_node = self.head
        
        if current_node == None:
            return False
        
        while current_node: 
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        len_ll = 0
        current_node = self.head

        while current_node != None:
            len_ll +=1
            current_node = current_node.next
        return len_ll

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        count = 0
        current_node = self.head

        while current_node != None:
            if count == index:
                return current_node.value
            count += 1
            current_node = current_node.next
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        head = self.head
        if head == None:
            return None

        while head.next:
            head = head.next
        
        return head.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head == None:
            self.add_first(value)
        else:
            new_node = Node(value)
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node


    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None
        
        head = self.head
        max_value = self.get_at_index(0)

        while head:
            if head.value > max_value:
                max_value = head.value
            head = head.next

        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def delete(self, value):

        new = self.head

        if new != None:
            if new.value == value:
                self.head = new.next
                new = None
                return

            while new:
                if new.value == value:
                    break
                prev = new
                new = new.next
            if new == None:
                return
            
            prev.next = new.next
            new = None


    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if not self.head:
            return
        current_node = self.head
        previous_node = None

        while current_node:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next

        self.head = previous_node

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
