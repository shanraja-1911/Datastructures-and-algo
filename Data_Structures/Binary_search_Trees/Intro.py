#Binary Search Trees are a non-linear data structure.
#They consist of a root node and zero, one or two children where the children can again have 0,1, or 2 nodes as their children and so on
#In most cases, the time complexity of operations on a BST, which include, lookups, insertions and deletions, take O(log N) time
#Except for the worst case, where the tree is heavily unbalanced with all the nodes being on one side of the tree.
#In that case, it basically becomes a linked list and the time complexities go up to O(n)

#Lets implement an unbalanced Binary Search Tree first
#We will need a node class to store information about each node
#It will store the data and the pointers to its left and right children

class Node():
  def __init__(self,data):
    self.data=data
    self.left=None 
    self.right=None

#Now we will implement the Binary Search Tree having a constructor with the root node initialised to None
#And the three methods, lookup, insert and delete

class BST():

  def __init__(self):
    self.root=None
    self.no_of_nodes=0 

  #For the insert method, we check if the root node is None, then we make the root node point to the new node
  #Otherwise, we create a temporary pointer which points to the root node at first.
  #Then we compare the data of the new node to the data of the node pointed by the temporary node.
  #If it is greater then first we check if the right child of the temporary node exists, if it does, then we update the temporary node to its right child
  #Otherwise we make the new node the right child of the temporary node
  #And if the new node data is less than the temporary node data, we follow the same procedure as above this time with the left child.
  #The complexity is O(log N) in avg case and O(n) in worst case.
  def insert(self,data):

    new_node=Node(data)

    if self.root == None:
      self.root=new_node
      self.no_of_nodes+=1
      return 
    
    else:
      current_node=self.root
      while (current_node.left!=new_node) and (current_node.right!=new_node):

        if current_node.data<new_node.data:
          
          if current_node.right ==None:
            current_node.right=new_node

          else :
            current_node=current_node.right

        elif current_node.data>new_node.data:

          if current_node.left==None:
            current_node.left=new_node

          else:
            current_node=current_node.left
      self.no_of_nodes+=1
      return 

  #Now we will implement the lookup method.
  #It will follow similar logic as to the insert method to reach the correct position.
  #Only instead of inserting a new node we will return "Found" if the node pointed by the temporary node contains the same value we are looking for

  def search(self,data):

    current_node=self.root

    while current_node.data!=data:

      if (current_node.data < data) and (current_node.right!=None) :
        current_node=current_node.right

      elif (current_node.data > data) and (current_node.left!=None):
        current_node=current_node.left 

      else :
        return "item not found" 
    
    
    return "item found" 


  # Remove the element form a binary 


    
    
    

    

if __name__=='__main__':
  a=BST()
  a.insert(10)
  a.insert(1)
  a.insert(5)
  a.insert(15)
  a.insert(14)
  a.insert(16)
  a.insert(18)


  #print(a.root.right.data)



  print(a.search(15))
  #a.search(2)
