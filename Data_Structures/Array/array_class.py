class Array:

  def __init__(self):
    self.len=0
    self.data={}

    #The attributes of the array class are stored in a dictionary by default.
    #When the __dict__ method is called on an instance of the class it returns the attributes of the class along with their values in a dictionary format
    #Now, when the instance of the class is printed, it returns a class object with its location in memory.
    #But we know when we print the array we get the elements of the array as output
    #When we print the instance of the class, the built-in __str__ method is called. So we can modify the __str__ method inside the class
    #To suit our needs.
  def __str__(self):
    return str(self.__dict__) #This will print the attributes of the array class(length and dsata) in string format when print(array_instance) is executed


  # Insert 
  def insert(self,index,item):
    self.len+=1
    for i in range(self.len-1,index,-1):
      self.data[i]=self.data[i-1]
    self.data[index]=item

  # look up 
  def get(self,index):
    return self.data[index]

  # Pop
  def pop(self):
    last_item=self.data[self.len-1]
    self.len-=1
    return last_item
  
  #delete
  def delete(self,index):
    for i in range(index, self.len-1):
      self.data[i]=self.data[i+1]
    
    del self.data[self.len - 1] #The last element which remains two times in the array is deleted

    self.len-=1
  
  # push
  def push(self,item):
    self.data[self.len]=item
    self.len+=1

   
arr=Array()
arr.push('hi')
arr.push("hello")
print(arr.get(0))
print(arr.pop())
arr.insert(0,0)
print(arr)


