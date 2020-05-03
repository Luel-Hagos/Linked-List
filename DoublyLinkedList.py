'''
Creating the Node class.
'''
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = None
        self.prev = None

'''
Creating the Single Linked List class.
'''
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    '''
    Inserts a node at the beginning of the List.
    Time Complexity: O(1).
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def insert_at_beginning(self, item): 
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        temp = self.head
        self.head = new_node
        self.head.next = temp
        temp.prev = self.head
        
    '''
    Inserts a node at the end of the List.
    Time Complexity: O(n), for scanning the list of size n.
    Space Complexity: O(1), for creating a temporary variable.
    '''   
    def insert_at_end(self, item): 
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        self.tail = new_node
        
    '''
    Inserts a node at any position of the List (at the beginning,at the end and between).
    Time Complexity: O(n), since, in the worst case, we may need to insert the node at the end of the list.
    Space Complexity: O(1), for creating one temporary variable.
    '''
    def insert_at_any_position(self, item, pos):
        new_node = Node(item)
        cur = 1
        temp = self.head
        # Inserting at the beeginning
        if pos == 1:
            self.head = new_node
            if temp == None:
                self.tail = new_node
                return
            self.head.next = temp
            temp.prev = self.head
            return
        while temp.next and cur < (pos-1):
            temp = temp.next
            cur += 1
        if pos > (cur + 1) or pos == 0:
            print("Can't insert! Desired position does not exist!")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next , self.tail = new_node , new_node 
                
    '''
    Deleting the first node of the List.
    Time Complexity: O(1).
    Space Complexity: O(1), for creating a temporary variable.
    '''
    def delet_first_node(self):
        if self.head == None:
            print('Can\'t delete! List is empty.')
            return
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp = None   
        
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
        while temp.next:
            temp = temp.next
        self.tail = temp.prev
        self.tail.next = None
        
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
        cur = 1
        # From beginning
        if pos == 1:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            temp = None
            return
        # Traverse the list untill arriving at the position from which we want to delete. 
        while temp.next and cur < pos:
            temp = temp.next
            cur += 1
        if pos != cur:
            print("Can\'t delete! Desired position does not exist!")
            return
        temp1 = temp.prev
        temp1.next  = temp.next
        if temp.next:
            temp.next.prev = temp1
            temp = None  
        return
    
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

list_ = DoublyLinkedList()
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