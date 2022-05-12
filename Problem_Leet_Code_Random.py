def oddseries(nums = int()):
  
  #Variables::
  
  #Creates a list of the numbers as individual variables
  nums_list = [int(i) for i in str(nums)]

  #Filters the first digit of the number
  x = nums_list[0:1:1]
  
  #Converts the first number to a string in the list
  y = [str(i) for i in x]
  
  #Creates a list to append the odd values
  z = []
 
  d = str(nums)
  #Gets the length of the number
  n = len(str(nums)) 
  
  #Extracts the first number from the list into a string, then converts it into a integer
  result = str("".join(y))
  first_digit = int(result)


  if first_digit % 2 != 0:
    z.append(first_digit)
  
  for i in nums_list:
    pre = nums_list.index(i)-1
    post = nums_list.index(i)+0
    if int(nums_list[pre]) % 2 != 0 and nums_list[post] % 2 != 0:
       z.append(nums_list.index(i))
  
  return z
    # left has none (false Node), and i is odd add to new list
    #Iterate to next digit, and if it is odd add to the list
    #if next digit is even create a new list
    #Iterate the next value to check if it is odd and check until no moree digits left in. the number
    #Convert both lists to integers and compoare the values
    #Return the larger value as the answer

oddseries(534456)