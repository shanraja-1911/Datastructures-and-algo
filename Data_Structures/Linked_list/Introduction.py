
#Linked lists are, as the name suggests, a list which is linked.
#It consists of nodes which contain data and a pointer to the next node in the list.
#The list is connected with the help of these pointers.
#These nodes are scattered in memory, quite like the buckets in a hash table.
#The node where the list starts is called the head of theblist and the node where it ends, or last node, is called the tail of the list.
#The average time complexity of some operations invloving linked lists are as follows:
#Look-up : O(n)
#Insert : O(n)
#Delete : O(n)
#Append : O(1)
#Prepend : O(1)
#Python doesn't have a built-in implementation of linked lists, we have to build it on our own
#So, here we go.


#First we define a class Node which will act as a blueprint for each of our nodes

class Node():
  def __init__(self,data):
    self.data=data 
    self.next=None

class Linked_list():

  def __init__(self):
    self.length=0
    self.head=None 
    self.tail=self.head

  # append method 
  #Next comes the append method with which we will add nodes to the end of the linked list.
  #To do this, we will just pass the data we want to append. The append method will create a new instance of the Node class,
  #Effectively creating a new node, with the data passed to the instance, so that the new node will contain the data the user wantsto enter
  #Then we will check if the list is empty. If it is, we will point the head to the new node just created and the tail to the head,
  #as there is only one node in the list, so the head and tail point to the same node. Also, we will set the length equal to 1.
  #If the list isn't empty, then we will make the 'next' pointer of the last node(pointed at by 'tail') point to the new node
  #And update the tail to point to the new node as this has become the last node in the list now. And we'll increase the length.

  def append(self,data):
    new_node=Node(data)
    if self.head==None:
      self.head=new_node
      self.tail=self.head
      self.length=1

    else:
      self.tail.next=new_node
      self.tail=new_node
      self.length+=1
    #print(self.head,new_node.data)

  #Next operation we'll implement is prepend, wehre we add a node at the head of the list.
  #For this, we will call the prepend method and pass the value we want to enter, which will create a new object of the node class
  #Then we will make the 'next' of the new node point to the head ,as the head iscurrently pionting to the first node of the list
  #And then we will update the head to point to new node as we want the new node to be new first node, i.e, the new head.
  #And ofcourse, we'll increase the length by 1

  def prepend(self,data):
    new_node=Node(data)

    if self.head==None:
      self.head=new_node
      self.head=self.tail
      self.length=1
    
    else:
      new_node.next=self.head
      self.head=new_node
      self.length+=1

  #Now we will implement the print function to print the values in the nodes of the linked list
  #We will check if the list is empty or not. If it is, we will printout "Empty"
  #Else, we will create a new node which will point to the head. Then we will loop until the node we created becomes None
  #Inside the loop we will print the data of the current node and then make the current node equal to the node pointed by the current node
  #Since this requires us to traverse the entire lenth og the linked list, this is an O(n) operation.

  def print_list(self):

    if self.head==None:
      print("Linked list empty")
    
    else:
      start=self.head
      while start!=None:
        print(start.data)
        start=start.next
        
    #Next comes the insert operation, where we insert a data at a specified position
    #If the position is greater than the length of the list, we simply follow the procedure of the append method where we add the node to the end of the list
    #If the position is equal to 0, we follow the prepend procedure, where we append the node at the head
    #If the postition is somewhere in between, then we create a temporary node which traverses the list upto the previous position of the position we want to enter the new node
    #Now the 'next' of the temporary node is pointing to the next node in the list, wehre we want to insert our new node#So first we link the new node and the node at the desired position by making the 'next' of the new node equal to the 'next' of the temporary node
    #The temporary node and the new node point to the same position now, the position we want to insert the new node
    #So we update the 'next' of the temporary node to point to the new node.
    #This way, our new node occupies the position it intended to and the node which was originally there, gets pushed to the next position
    #Since this requires traversal of the list, it is an O(n) operation.

  def insert(self,index,value):
    if index >self.length-1:
      print('The index does not exist, so adding it at the end')
      self.append(value)
    
    # elif index == self.length-1:
    #   print('adding it at the end')
    #   self.append(value)

    else :
      count=0
      new_node=Node(value)
      current_node=self.head
      while count <index-1:
        current_node=current.next
        count+=1
      
      new_node.next=current_node.next
      current_node.next=new_node
      self.length+=1

#Next comes the delete_by_value method where the user can enter a value and if the value is found in the list, it will be deleted.
#(If the value is found multiple times, only the first occurence of thevalue will be deleted.)
#First we check if the list is empty. If yes, we print appropriate message. If not, then we create a temporary node.
#Then we check if the value of the head is equal to the value we want deleted.
#If yes, we make the head equal to the node pointed by the 'next' of the head. Then we check if there are only one or zero nodes in the list
#If yes, then we update the tail to be equal to the head.
#By Doing this, the original 'head' gets disconnected from the list and the head becomes updated to what was originally the second node
#If these two cases are not encountered, then we have to traverse the list and check every node.
#So we loop until either the current node becomes None, signifying the end of the list, or until the data of the node next to the current node equals the data we want deleted.
#After coming out of the loop we check if the current node is not equal to None, it means the next node of the current node is the one we want deleted
#So we make the 'next' of the current node point to the next to the next of the current node.
#Effectively, we bypass the node we want deleted and establish a connection between the current and the next to next of the current nodes.
#After deleting the required node, we check if the current node's 'next' points to None, i.e., if it is the last node. If yes, then we update the tail
#And if the current node is None, it means we traversed the entire list but couldn't find the value.

  def delete(self,value):

    current_node=self.head

    if self.head==None:
      return 

    elif current_node.data==value:
      self.head=current_node.next
      self.length-=1

    elif self.tail.data==value:
      for i in range(self.length-2):
        current_node=current_node.next
    

      self.tail=current_node
      self.tail.next=None
      self.length-=1

    while current_node.next !=None:
      
      if (current_node.next.data == value)&(current_node.next.next != None):
        current_node.next=current_node.next.next
        self.length-=1
      current_node=current_node.next

  def del_by_pos(self,pos):
    current_node=self.head
    if pos==0:
      self.head=self.head.next
      self.length-=1
    elif pos<0:
      print('enter a valid number')
      return
      
    elif pos>=self.length:
      print('Enter a valid position')
      
    elif pos==self.length-1:
      for i in range(self.length-2):
        current_node=current_node.next
      
      self.tail=current_node 
      self.tail.next=None
      
    else:
      for i in range(pos-2):
        current_node=current_node.next
        
      current_node.next=current_node.next.next
      self.length-=1 
    

  
#Another functionality of linked lists can be deleting a node based on its position.
#It follows more or less the same procedure as delete_by_value method.
#Only real difference is instead of traversing the list till the current node becomes None or the next node equals the required data,
#Here we traverse the list till the position one place behind the position we want deleted, similar to the insert operation
#And then we bypass the next node to the current node and link it to the next to the next node of the current node.
#We do a similar check for tail and update it just like in the delete_by_value method.
#This operation too has a time complexity of O(n) in the worst case.

     


  
  



      




#We will import this file while reversing a linked list. So we must make sure that it runs only
#when it is the main file being run and not also when it is being imported in some other file.
if __name__=='__main__':

  obj=Linked_list()
  obj.append(5)
  obj.append(10)
  obj.insert(1,11)
  #obj.delete(10)
  obj.del_by_pos(-2)
  


  obj.print_list()




