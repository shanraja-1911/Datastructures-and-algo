# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.


tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]



def min_rotation(tops, bottoms):
  #get the first value from the top and the one from the bottom
  top_val=tops[0]
  bottom_val=bottoms[0]
  len_arr=len(tops)
  flag=0


  #print(len_arr)

  # create an array to capture if the top val exist in top and bottom list
  top_val_in_tops= [1 if x==top_val else 0 for x in tops ]
  top_val_in_bottom= [1 if x==top_val else 0for x in bottoms ]

  

  # check if the condition sum of the result is equal to the len of array is met 
  if sum([a or b for a,b in zip(top_val_in_tops, top_val_in_bottom)])== len(tops):
    # return the minimum of( len(arr)- sum (calculated array)) for both the lists
    flag+=1
    upper_val= min (len_arr-sum(top_val_in_tops), len_arr-sum(top_val_in_bottom))
  
  

  # create an array to capture if the bottom val exist in top and bottom list
  bot_val_in_tops= [1 if x==bottom_val else 0 for x in tops ]
  bot_val_in_bottom= [1 if x==bottom_val else 0 for x in bottoms]

  
  # check if the condition sum of the result is equal to the len of array is met 
  if sum([a or b for a,b in zip(bot_val_in_tops, bot_val_in_bottom)])== len(tops):
    # return the minimum of( len(arr)- sum (calculated array)) for both the lists
    lower_val = min (len_arr-sum(bot_val_in_tops), len_arr-sum(bot_val_in_bottom))
    flag+=2

  if flag==2:
    return lower_val
  elif flag==1:
    return upper_val
  elif flag==3:
    return min (upper_val,lower_val)
  else:
    return -1







if __name__=='__main__':
  print(min_rotation(tops,bottoms))