'''
Creating the Node class.
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = self

'''
Creating the Single Linked List class.
'''
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    '''
    Inserts a node at the beginning of the List.
    Time Complexity: O(n), for scanning the complete list of size n.
    Space Complexity: O(1), for temporary variable.
    '''
    def insert_at_beginning(self, item): 
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
        return
   
    '''
    Inserts a node at the end of the List.
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    '''   
    def insert_at_end(self, item): 
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        return
    
    '''
    Deleting the first node of the List.
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def delet_first_node(self):
        if self.head == None:
            print('Can\'t delete! List is empty.')
            return
        temp = self.head
        temp1 = self.head
        if temp.next == self.head:
            del temp
            self.head = None
            return
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
        del temp1
        return
        
    '''
    Deleting the last node of the List.
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def delet_last_node(self):
        if self.head == None:
            print('Can\'t delete! List is empty.')
            return
        temp = self.head
        prev = self.head
        if temp.next == self.head:
            del temp
            self.head = None
            return
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head
        del temp
        return
    
    '''
    Prints each element of the list.
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def print_list(self):
        if self.head == None:
            print("Empty list!")
            return 
        temp = self.head
        current = None
        while True:
            print(temp.data, end = '-->')
            temp = temp.next
            if temp.next == self.head:
                break
        print(temp.data)
        return
        
    '''
    Returns the length of the list (total number of elements).
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    ''' 
    def len_of_list(self): 
        count = 0
        temp = self.head
        if self.head == None:
            return count
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count
    
list_ = CircularLinkedList()
list_.insert_at_end(1)
list_.insert_at_end(2)
list_.insert_at_end(3)
list_.print_list()
print("Length of list:", list_.len_of_list())
print()
list_.insert_at_beginning(0)
list_.print_list()
print("Length of list:", list_.len_of_list())
print()
list_.delet_first_node()
list_.print_list()
print("Length of list:", list_.len_of_list())
print()
list_.delet_last_node()
print()
list_.print_list()
print("Length of list:", list_.len_of_list())