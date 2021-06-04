#Rachel Ki
# Part A
def str_to_list(my_str):
    '''
    str_to_list() takes a string as an input parameter.
    - If the string has an even number of characters, return two lists,
      one containing each character of the first half of the string
      and the other containing each character of the second half of the string.
    - If the string has an odd number of characters, return two lists that
      cut the string in half as above. Odd strings will have lengths 2n+1.
      When returning, have the first list contain the first n+1 characters
      and the second list contain the last n characters.
    '''
    # Two blank lists to begin
    list1 = []
    list2 = []
    
    #halfnum is the number that splits the string in half. When odd, the list in front has more values.
    if len(my_str) % 2 == 1:
        halfnum = (len(my_str) // 2) + 1
    else:
        halfnum = len(my_str) // 2
    
    #list1 is the list with the first half of the string
    for i in my_str[:halfnum]:
        list1.append(i)
    
    #list2 is the list with the second half of the string
    for j in my_str[halfnum:]:
        list2.append(j)
        
    return (list1,list2)


def list_nester(my_lst):
    '''
    list_nester() takes a list as an input parameter.
    - Return a list that contains each element from the input list
      nested into another list.
    - If an empty list is passed into the function as the argument,
      return an empty list.
    '''
    #newlist that will append each nested elements
    newlist = []
    
    #for loop that appends each elements nested
    for i in my_lst:
        newlist.append([i])
    
    return newlist


# Part B
def perimeter_sum(my_array):
    '''
    perimeter_sum() takes an NxM nested list containing integers as input.
    - The function calculates the sum around the "perimeter" of the array
      and returns this value.
    '''
    #set the sum for 0, this would add up the sum around the perimeter of the array
    sum = 0
    
    #calculate the sum of the top row
    for i in my_array[0]:
        sum += i
        
    #calculate the sum of the bottom row
    for j in my_array[-1]:
        sum += j
    
    #calculate the first and last letters of the intermediate rows
    for intermediate in my_array[1:-1]:
        sum += intermediate[0] + intermediate[-1]
        
    return sum
