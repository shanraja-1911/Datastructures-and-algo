# import the helper fucntion from introduction 
from Introduction import Node,Linked_list


### The first attemp at this problem is in-effcient 
# get the current_node_right
def get_current_node_right(x,lst):
  pointer=lst.head
  for i in range(lst.length-x-2):
    # print(f"i value {i}")
    pointer=pointer.next

  # print(f'the pointer data is {pointer.data}')
  return pointer






# reversing the list 
def reverse(lst):
  len_lst=lst.length
  if len_lst<1:
    return lst
  current_node_left=lst.head
  current_node_right=lst.tail

  for x in range(int(len_lst/2)):
    # print(f'the value of x is {x}')
    temp=current_node_left.data
    current_node_left.data=current_node_right.data
    current_node_right.data=temp
    current_node_left=current_node_left.next
    current_node_right=get_current_node_right(x,lst)

  return lst


### efficient solution using 2 pointers


def reverse_efficient(lst):
  prev,curr=None,lst.head

  while curr:
    temp=curr.next
    curr.next=prev
    prev=curr
    curr=temp

  lst.head=prev
  return lst




lst=Linked_list()
lst.append(10)
lst.prepend(11)
lst.prepend(114)
lst.insert(12,1)
lst.append(13)
lst.print_list()
print('the reversed list is ')
reverse(lst).print_list()
print('the reversed list efficient is ')
reverse_efficient(lst).print_list()
print('the Original list is ')
lst.print_list()

