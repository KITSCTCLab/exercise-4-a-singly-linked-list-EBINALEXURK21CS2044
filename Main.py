class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def append(self,x):
        newNode=node(x)
        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newNode
    def appendAfter(self,prev,x):
        temp=self.head
        midNode=node(x)
        if temp is None:
            print("The Linked List is empty")
        while temp.data!=None:
            if temp.data==prev:
                tempNode=temp.next
                temp.next=midNode
                midNode.next=tempNode
                break
            elif temp.next==None:
                print("%d not in the linked list" % prev)
                break
            else:
                temp=temp.next
    def deleteLast(self):
        temp=self.head
        if self.head==None:
            print("Empty list")
            return
        elif self.head.next==None:
            print("The deleted data is: ",self.head.data)
            del self.head
            self.head=None
            return
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
        
        print("The data deleted is: ",temp.data)
        del temp
    def deleteSpec(self,d):
        temp=self.head
        if self.head==d:
            self.head=self.head.next
        else:
            while temp!=None and temp.data!=d:
                prev=temp
                temp=temp.next
        if temp==None:
            print("No value found")
        else:
            prev.next=temp.next
            
        print(d, 'was deleted')
        del temp
    def display(self):
        temp=self.head
        
        if temp==None:
            print("Empty Linked List")
            return
        while temp.next!=None:
            print(temp.data, end=" --> ")
            temp=temp.next
        print(temp.data, end=" --> ")
        print(None)
        
list1=linkedList()
while (1):
    print("\nOptions:\n1. Add Data\n2. Insert After\n3. Delete End Data\n4. Delete specified data\n5. Display\n6. Exi
    userch=int(input("Enter your choice: "))
    if userch==1:
        data=int(input("Enter data to insert: "))
        list1.append(data)
    elif userch==2:
        list1.display()
        prev=int(input("After which data would you like to insert: "))
        data=int(input("Enter data to insert: "))
        list1.appendAfter(prev,data)
    elif userch==3:
        list1.deleteLast()
    elif userch==4:
        data=int(input("Enter data to delete: "))
        list1.deleteSpec(data)
    elif userch==5:
        list1.display()
    elif userch==6:
        print("Thank You!")
        break
    else:
        print("Sorry, Option not Found")
        
        
