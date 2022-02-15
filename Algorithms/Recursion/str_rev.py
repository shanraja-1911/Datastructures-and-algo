# String reversal using recursion 

# remove the first letter and add it to the end 


def str_rev(name):
  if len(name)==0:
    return name
  return str_rev(name[1:])+name[0]


def str_rev_iter(name):

  rev_name=''
  for i in range(len(name)):
    rev_name+=name[len(name)-1-i]
  return rev_name


if __name__=='__main__':
  print(str_rev('shan'),str_rev_iter('shan'))