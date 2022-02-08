# Factorial using recusrsion 

def Factorial_rec(num):
  if num==0:
    return 1
  return num*Factorial_rec(num-1)


def Factorial_iter(num):
  mul=1
  while num!=0:
    mul*=num
    num-=1

  return mul


if __name__=='__main__':

  test_num=100

  print(Factorial_rec(test_num),Factorial_iter(test_num))