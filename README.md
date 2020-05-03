# Linked List

* This repository contains the basic operations of linked lists.

A __linked list__ is a linear data structure where each element is a separate object.

Each element (a __node__) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to __null__. The entry point into a linked list is called the __head__ of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand. Any application which has to deal with an unknown number of objects will need to use a linked list.

One disadvantage of a linked list against an array is that it does not allow direct access to the individual elements. If you want to access a particular item then you have to start at the head and follow the references until you get to that item.

Another disadvantage is that a linked list uses more memory compare with an array - we extra 4 bytes (on 32-bit CPU) to store a reference to the next node.

### Types of Linked Lists
* A __singly linked list__ a sequence of elements in which every element has link to its next element in the sequence ( it is described above).

![](https://github.com/Luel-Hagos/T/blob/master/Image/Singlyimage.PNG)

* A __doubly linked list__ is a list that has two references, one to the next node and another to previous node ( items can be navigated forward and backward ).
![](https://github.com/Luel-Hagos/T/blob/master/Image/doublyimage.PNG)

* A __circular linked list__ where last node of the list points back to the first node (or the head) of the list.
![](https://github.com/Luel-Hagos/T/blob/master/Image/Curcularimage.PNG)

__Example__: if we run the [SinglyLinkedList.py](https://github.com/Luel-Hagos/Linked-List/blob/master/SinglyLinkedList.py) on any python environment we will get the following output.
![](https://github.com/Luel-Hagos/T/blob/master/Image/singly.PNG)

__See also__ [Wikipedia](https://en.wikipedia.org/wiki/Linked_list) and [tutorialspoint](https://www.tutorialspoint.com/data_structures_algorithms/linked_list_algorithms.htm)
