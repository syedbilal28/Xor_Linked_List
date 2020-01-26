# Xor_Linked_List
python implementation of xor linked list by simulating pointers on dictionary data structure.

Note: as pointers can't be accessed directly in python so the assumption here is made that every node in the linked list takes 6 memory block addresses.

The XOR.py file holds the source code to the implemetation. 
The following Functions are defined against their respective behavior.

InsertAtFirst(self,value):
        """Inserts Data at the beginning of the list and makes it head"""
InsertAtLast(self,value):
        """Inserts data at the end of the list and makes it tail"""
Print(self):
        """Prints the entire data in the list"""
Get(self,index):
        """Return the value against the index asked"""
DeleteAtEnd(self):
        """Deletes the item at the end of the list and reduces tail"""
DeleteAtFirst(self):
        """Deletes the item at the start of the list and increases head"""
Length(self):
        """returns length of list"""
InsertAfter(self,value,item):
        """Inserts an item after a value given by the user"""
DeleteByValue(self,value):
        """Deletes Node by the value given"""
