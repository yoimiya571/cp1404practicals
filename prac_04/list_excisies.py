numbers = []
for i in range (5):
    number = int(input("Number:1"))
    numbers.append(number)

print("the first number is ", numbers[0])
print("the last number is", numbers[-1])
print("the smallest number is", min(numbers) )
print("the largest number is", max(numbers))
print("the average of numbers is", sum(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


username  = input("enter your username")
if username in usernames:
    print("access granted")
else:
    print("access denied")