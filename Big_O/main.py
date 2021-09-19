 # Import the libraries  
import time 


start =time.time()

nemo=['nemo']

def find_newo(lst):
  for x in lst:
    if x=='nemo':
      print(f'found nemo')

find_newo(nemo)



end=time.time()
print(f'elapsed time {end - start }')
