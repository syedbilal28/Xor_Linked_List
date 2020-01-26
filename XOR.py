class XNode:
    def __init__(self,value):
        self.npx = 0
        self.Data = value

class XORLinkedList:
    def __init__(self):
        self.data = {}
        self.head = 1000
        self.tail = 1000
    def InsertAtFirst(self,value):
        """Inserts Data at the beginning of the list and makes it head"""
        x= XNode(value)
        #print(self.head)
        if self.head!= self.tail: # to Check that it's not an empty list
            self.data[self.head+6].npx=self.head^self.head+12
        try:
            next = (self.data[self.head+6])
            next = self.head+6
        except:
            next =0

        prev = 0
        #print(prev,next,"\n----------------------")
        x.npx = prev^ next

        self.data[self.head] = x

        self.head -= 6

    def InsertAtLast(self,value):
        """Inserts data at the end of the list and makes it tail"""
        x= XNode(value)
        self.tail += 6
        if self.head ==self.tail: # Checks that the list is not empty
            x.npx = 0
            self.data[self.tail] = x
        else:
            next = 0
            try:
                prev = (self.data[self.tail - 6])
                prev = self.tail - 6

            except:
                prev = 0
            try:
                prev_ = self.data[self.tail - 12]
                prev_= self.tail-12
            except:
                prev_ = 0
            self.data[self.tail - 6].npx = self.tail ^ prev_


            x.npx= prev^ next
            self.data[self.tail]=x

    def Print(self):
        """Prints the entire data in the list"""
        x= self.head+6

        prev= 0

        while prev!= self.tail:# traversal code

            print(self.data[x].Data)


            next = prev ^ self.data[x].npx
            prev = x
            x= next
    def Get(self,index):
        """Return the value against the index asked"""
        x = self.head + 6

        prev = 0
        data= -1
        for i in range(index + 1):# Traverses towards the index given
            # print(x)
            data = self.data[x].Data

            next = prev ^ self.data[x].npx
            prev = x
            x = next
        return data
    def DeleteAtEnd(self):
        """Deletes the item at the end of the list and reduces tail"""
        self.data.__delitem__(self.tail)
        self.tail-=6
        self.data[self.tail].npx = self.tail-6 ^0
    def DeleteAtFirst(self):
        """Deletes the item at the start of the list and increases head"""
        self.data.__delitem__(self.head+6)
        self.head += 6
        self.data[self.head+6].npx = 0 ^ self.head+12
    def Length(self):
        """returns length"""
        return int((self.tail-(self.head))/6)
    def _Fixing(self,head,pattern):
        tail = self.tail


        while head <=tail:

            if tail==self.tail:
                self.InsertAtLast(self.data[self.tail].Data)
            else:
                self.data[tail+pattern] = self.data[tail]
                self.data[tail+pattern].npx = tail^(tail+(2*pattern))
            print(tail+pattern,self.data[tail+pattern].Data,self.data[tail+pattern].npx)
            tail-=6
        #print(self.data)
    def InsertAfter(self,value,item):
        """Inserts an item after a value given by the user"""
        c= XNode(item)
        x = self.head + 6

        prev = 0

        while prev != self.tail:#Traversal
                # print(x)
            if self.data[x].Data == value:

                self._Fixing(x+6,6)
                self.data[x+6] =c
                c.npx=(x)^x+12
                self.tail+=6
                break

            next = prev ^ self.data[x].npx
            prev = x
            x = next
    def _DelFix(self,end,pattern):
        temp = self.data[self.head+ 6]
        self.data.__delitem__(self.head+6 )

        head= self.head+6
        while end >= head:
            try:
                prev=self.data[end - 6]
                self.data[end] = self.data[end - 6]
                self.data[end].npx = (end - pattern) ^ (end + pattern)

            except:
                prev=0
                self.data[end] = temp
                self.data[end].npx = (prev) ^ (end + pattern)
                #print(end, self.data[end].Data, self.data[end].npx)
                break


            #print(end , self.data[end].Data, self.data[end].npx)
            end -= 6
    def DeleteByValue(self,value):
        """Deletes Data by the value given"""
        x = self.head + 6

        prev = 0

        while prev != self.tail:

            if self.data[x].Data == value:
                if x == self.head+6:
                    #print("Hereee")
                    self.DeleteAtFirst()
                    break
                elif x== self.tail:
                    self.DeleteAtEnd()
                    break
                self._DelFix(x, 6)
                self.head += 6
                break

            next = prev ^ self.data[x].npx
            prev = x
            x = next


