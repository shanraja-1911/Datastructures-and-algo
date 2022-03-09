# Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

lst=[1,2,3,4]

def find_product(lst):
    # get the mutilplied value of the list
    mult_val=1
    flag=-1 
    for val in lst:
        if val !=0:
            mult_val*=val
        else:
             flag+=1

    # Divide the mutiplied value with each of the value
    for index,val in enumerate(lst):
        if (val==0) and (flag<1):
            lst[index]=mult_val
            flag+=1
        
        elif (val!=0) and (flag<1):
            
            lst[index]=mult_val/val

        else:
            lst[index]=0

    return lst


if __name__=='__main__':
  print(find_product(lst))



  