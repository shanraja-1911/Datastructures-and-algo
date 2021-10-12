# Array implementation of the stacks 
#Stacks can be implemented with th ehelp of arrays as well.
#We can insert and delete elements only at the end of the array(the top of the stack)
#Python comes built-in with lists which are basically arrays.
#They contain functionalities like append and pop which correspond to the push and pop methods of stacks respectively
#So implementing stacks using arrays is pretty simple in Python
#The time complexities of different operations are same as that for the inked list implementation of stacks

# create a class named stack 

class Stack():

  #The constructor consists of only an empty array as length comes built-in with arrays(lists)
  def __init__(self):
    self.array=[]

  #In the peek method we access the last element of the array(top element of the stack) by using the built-in length functionality of arrays
  def peek(self):
    return self.array[-1]

  def push(self,data):
    self.array.append(data)
    return 

  #For pop operation, we use thebuilt-in pop method of lists, which removes the last element of the list(top element of the stack)
  #Time complexity of pop operation for the last element of the list is O(1).
  def pop(self):
    if len(self.array)!=0:
      self.array.pop()
      return 
    else:
      print('empty stack')
      return 

  #Stack follows LIFO, so for the print operation, we have to print the last element of the list first.
  #This will require a loop traversing the entire array, so the complexity is O(n)
  def print_stack(self):
    if len(self.array)!=0:
      for x in self.array:
        print(x)
      return 
    else :
      print('empty stack')

if __name__=='__main__':
  stck=Stack()
  stck.push(10)
  stck.print_stack() 
  print(stck.peek())
  stck.pop()
  stck.print_stack()

'''Stacks can be implemented in Python in two more ways.
1. Using the 'deque' class from 'collections' module. Same methods used in lists, append and pop are used in deques
2. Using 'LifoQueue' from the 'queue' module . 'put()' and 'get()' methods are used for pushing and popping. It comes with some other useful metjods async well. 
'''