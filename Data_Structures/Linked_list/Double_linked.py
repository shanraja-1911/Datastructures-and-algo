#Doubly linked lists are just normal, singly linked lists with one added feature,
#a link to the previous node as well in addition to a link to the next node.
#Although the worst case time complexities of all operations in a doubly linked list are same as that of a singly linked list,
#Some operations are technically faster. For example, lookup or searching, is O(n/2) as search can begin from both ends
#But O(n/2) = O(n), so it is still the same as that for a singly linked list.

#Implementation of doubly linked list is almost exactly the same as that for singly linked list,
#With just the added feature of the pointer to the previous node.
#We'll have the same methods which do the exact same thing. The pars which will be different from the singly linked list are explained
#So lets implement it.

class Node():
  def __init__(self,data):
    self.data=data 
    self.next=None 
    self.previous=None


class Double_Linked():

  def __init__(self):
    self.head=None 
    self.tail=None
    self.length=0

  def print_list(self):
    if self.length==0:
      print('The linked list is empty')

    
    else:
      current_node=self.head
      while current_node!=None:
        print(current_node.data)
        current_node=current_node.next
  
  def prepend(self,data):
      new_node=Node(data)
      if self.head==None:
        self.head=new_node
        self.tail=self.head
        self.length+=1
      else :
        self.previous=new_node
        new_node.next=self.head
        self.head=new_node
        self.length+=1
        
  def append(self,data):
    new_node=Node(data)

    if self.head==None:
      print('The list is empty, so adding it as the head')
      self.head=new_node
      self.tail=self.head
      self.length+=1

    else:
      new_node.previous=self.tail
      self.tail.next=new_node
      self.tail=new_node
      self.length+=1

  def delete_by_val(self,val):

    if self.head==None:
      print('the list is empty')

    elif self.head.data==val:
      self.head=self.head.next
      self.previous=None
      self.length-=1

    elif self.tail.data==val:
      self.tail=self.tail.previous
      self.tail.next=None
      self.length-=1
    
    else:
      current_node=self.head
      while current_node!=None:
        if current_node.data==val:
          current_node.next.previous=current_node.previous
          current_node.previous.next=current_node.next
          self.length-=1
        current_node=current_node.next
  
    
  def insert(self,val,pos):
    if pos >= self.length:
      print('insert position exceeding the size, so appending data')
      self.append(val)

    elif pos==0:
      self.prepend(val)

    else :
      current_node=self.head
      new_node=Node(val)
      count=0
      while count==pos-2:
        current_node=current_node.next
        count+=1

      new_node.previous=current_node
      new_node.next=current_node.next
      current_node.next=new_node

       
      



if __name__=='__main__':

  DL=Double_Linked()
  DL.prepend(5)
  DL.append(10)
  #DL.delete_by_val(5)
  DL.insert(0,0)
  DL.print_list()
  