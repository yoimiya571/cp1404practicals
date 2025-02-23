numbers = [3,1,4,1,5,9,2]



numbers[0]  #the first element  of numbers
numbers[-1]  #the last element of numbers
numbers[3]   #the forth element of numbers
numbers[:-1]   #
numbers[3:4]
5 in numbers   #check if 5 is an element of numbers
7 in numbers  #check if 7 is an element of numbers
"3" in numbers  #check if "3" is an element of numbers
numbers + [6, 5, 3]


#Change the first element of numbers to "ten"
numbers[0] = "ten"
#Change the last element of numbers to 1
numbers[-1] = 1
#Print all the elements from numbers except the first two (slice)
numbers[2:]
#Print whether 9 is an element of numbers
9 in numbers