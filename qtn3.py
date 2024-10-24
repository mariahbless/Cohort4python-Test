# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
 
number= int(input("Enter the number here:"))
if number != 0 :
     print(f"Enter another number")
else :
   print( sum(number))





# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
for numbers in range(1,100):
 if numbers % 2 != 0:
   print(numbers)