 


# Big O
-----------

The notion of Big O  is used to measure the time complexity of an algorithm irrespective of the compute that it is running on.</br>

* O(n)- It is the linear time complexity. <br>

* O(1)- no matter the size of the input , it is the same or constant.<br>

# Rule to calculate Big O
______

* Rule 1: ** Worst case **<br>

  <p> Always think about the worst case scenario.<\p> 

* Rule 2: ** Remove Constant **

  <p> Ignore the constant value in the Big O notation. <\p>

* Rule 3: ** Different terms for inputs **

  <p> Lets suppose there are two input of varying sizes and there is a for loop for each of the input, then the O is O(len(a) +len(b).<\p>

* Rule 4: Drop Non-Dominants

  <p> If the bigO notation is a sum of complex terms, then just keep the dominant term. Eg: O(n+n^2)==O(n^2)
<\p>




