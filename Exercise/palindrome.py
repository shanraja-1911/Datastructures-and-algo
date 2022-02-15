def palindrome(num):
  # if number is negative , it cannot be a plaindrome
  if num <0:
    return False
  rev_num=0
  act_num=num
  while int(num/10) !=0:
    rev_num=(num%10)*10 + rev_num*10
    num=int(num/10)
    print(rev_num,num)
  rev_num+=num
  print(rev_num)
  return [True if rev_num==act_num else False][0]
  


def palindrome_str(num):

  num=str(num)

  for x in range(0,int(len(num)/2)):
    if num[x]!=num[int(len(num))-1-x]:
      return False 
    
  return True


if __name__=='__main__':
  print(palindrome(0),palindrome(1221),palindrome_str(121))
  
