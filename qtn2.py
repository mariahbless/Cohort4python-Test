# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

mark = int(input("Enter your marks here:"))
if mark >= 90 :
     print('The student is in Grade A')
elif mark >= 80 :
     print('The student is in Grade B')
elif mark >= 70 :
     print('The student is in Grade C')
elif mark >= 60 :
    print("The student is in Grade D")
elif mark >= 40 :
     print("The student is in Grade E")
elif mark < 40 :
     print("The student is in Grade F")