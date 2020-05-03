'''
Creating the Node class.
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
        
'''
Creating the Single Linked List class.
'''
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    '''
    Inserts a node at the beginning of the List.
    Time Complexity: O(1).
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def insert_at_beginning(self, item): 
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        self.head = new_node
        self.head.next = temp
        
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
        while temp.next:
            temp = temp.next
        temp.next = new_node

    '''
    Inserts a node at any position of the List (at the beginning,at the end and between).
    Time Complexity: O(n), since, in the worst case, we may need to insert the node at the end of the list.
    Space Complexity: O(1), for creating one temporary variable.
    '''
    def insert_at_any_position(self, item, pos):
        new_node = Node(item)
        cur = 1
        temp = self.head
        prev = None
        # Inserting at the beeginning
        if pos == 1:
            new_node.next = temp
            self.head = new_node
            return
        # Traverse the list until the position where we want to insert
        while temp and cur < pos:
            prev = temp
            temp = temp.next
            cur += 1
        # if the position is greater than the number of the elements of list, can't be inserted.
        if pos > (cur + 1) or pos == 0:
            print('Can\'t insert! position doesn\'t exist.')
            return
        prev.next = new_node
        new_node.next = temp
        
    '''
    Deleting the first node of the List.
    Time Complexity: O(1).
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def delet_first_node(self):
        if self.head == None:
            print('Can\'t delete! List is empty.')
            return
        temp = self.head.next
        self.head = None
        self.head = temp
        
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
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        temp = None
        prev.next = None
        
    '''
    Deleting a node at ant position of the List.
    Time Complexity: O(n). In the worst case, we may need to delete the node at the end of the list.
    Space Complexity: O(1), for one temporary variable.
    '''
    def delet_at_any_position(self, pos): 
        if self.head == None:
            print('Can\'t delete! List is empty.')
            return
        temp = self.head
        prev = None
        cur = 1
        # From beginning
        if pos == 1:
            self.head = self.head.next
            del temp
            return
        # Traverse the list untill arriving at the position from which we want to delete. 
        while temp and cur < pos:
            prev = temp
            temp = temp.next
            cur += 1
        if temp == None:
            print('Can\'t delete! position doesn\'t exist.')
            return
        temp = None
        prev.next = temp.next

        '''
    Deleting the Linked List.
    Time Complexity and Space Complexity : O(1).
    '''
    def clear_linked_list(self):
        self.head = None
        
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
    	while temp.next:
    		print(temp.data, end = '-->')
    		temp = temp.next
    	print(temp.data)
        
    '''
    Returns the length of the list (total number of elements).
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    ''' 
    def len_of_list(self): 
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    '''
    Reverse the linked list.
    Time Complexity: O(n).
    Space Complexity: O(1).
    '''
    def reverse_list(self):
        temp1, temp2 = None, None
        while self.head:
            temp1 = self.head.next
            self.head.next = temp2
            temp2 = self.head
            self.head = temp1
        self.head = temp2

    '''
    Display the List from the end.
    Time Complexity: O(n).
    Space Complexity: O(n)
    '''
    def print_from_end(self,head):
        if head == None:
            return
        self.print_from_end(head.next)
        print(head.data)

list_ = SinglyLinkedList()
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
list_.insert_at_any_position(4,5)
list_.print_list()
print("Length of list:", list_.len_of_list())
print()
list_.insert_at_any_position(8,0)
list_.print_list()
print("Length of list:", list_.len_of_list())
list_.delet_first_node()
print()
list_.print_list()
print("Length of list:", list_.len_of_list())
list_.delet_last_node()
print()
list_.print_list()
print("Length of list:", list_.len_of_list())
list_.delet_at_any_position(1)
print()
list_.print_list()
print("Length of list:", list_.len_of_list())
print("Printing from the end: ")
list_.print_from_end(list_.head)
print("\nreversed list")
list_.reverse_list()
list_.print_list()
print("Length of list:", list_.len_of_list())
list_.clear_linked_list()
print()
list_.print_list()
print("Length of list:", list_.len_of_list())