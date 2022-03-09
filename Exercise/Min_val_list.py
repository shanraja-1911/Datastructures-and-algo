# Given a list of size ‘n,’ can you find the minimum value in the list? Implement your solution in Python and see if your output matches the expected output.

lst=[9,2,3,6]

def find_minimum(arr):
    min_val=arr[0]
    for val in arr[1:]:
        if val<min_val:
            min_val=val
    return min_val


if __name__=='__main__':
  print(find_minimum(lst))