# Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:
#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                       B
#          >= 60 and <= 80                       C
#          below 60                                  D
x=int(input("Enter Percentage"))
if x>90:
    print('A')
elif x==80 & x<=89:
    print('B')
elif x==70 & x<=79:
    print('C')
else:
    print('D')

# Q2. Write a program to accept the cost price of a bike and
#  display the road tax to be paid according to the following criteria :
    
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                          10%
#         <= 50000                                                  5%
x=int(input("Enter cost"))
if x>100000:
    print('15%')
elif x>50000 & x<=100000:
    print('10%')
elif x<=50000:
    print('5%')
else:
    print('0%')

# Q3. Write a program to check whether a year is a leap year or not.
leap_year=int(input("Enter a year"))
if leap_year %2==0:
    print("This is a leap year")
else:
    print("This is not a leap year")

# Q4. Write a program to accept a number from 1 to 7 and display the name of the day
#  like 1 for Sunday , 2 for Monday and so on.
y=int(input("enter number between 1 to 7"))
if y==1:
        print(f"{y} is for sunday")
elif y==2:
        print(f"{y} is for Monday")
elif y==3:
        print(f"{y} is for Tuesday")
elif y==4:
        print(f"{y} is for Wednesday")
elif y==5:
        print(f"{y} is for Thursday")
elif y==6:
        print(f"{y} is for Friday")
elif y==7:
        print(f"{y} is for Saturday")
else:
        print("Please enter number between 1 to 7")




# Q5. Write a program to accept a number from 1 to 12 and display name of
#  the month and days in that month like 1 for January and number of days 31 and so on
x=int(input("enter number between 1 to 12"))
if x==1:
    print(f"{x} is January and the number of days is 31")
elif x==2:
    print(f"{x} is February and the number of days is 28 or 29")
elif x==3:
    print(f"{x} is March and the number of days is 31")
elif x==4:
    print(f"{x} is April and the number of days is 30")
elif x==5:
    print(f"{x} is May and the number of days is 31")
elif x==6:
    print(f"{x} is June and the number of days is 30")
elif x==7:
    print(f"{x} is July and the number of days is 31")
elif x==8:
    print(f"{x} is August and the number of days is 31")
elif x==9:
    print(f"{x} is September and the number of days is 30")
elif x==10:
    print(f"{x} is October and the number of days is 31")
elif x==11:
    print(f"{x} is November and the number of days is 30")
elif x==12:
    print(f"{x} is December and the number of days is 31")






# Q6. Write the logical expression for the following:
# A is greater than B and C is greater than D
print('A'>'B' and 'C'>'D')

# Q7. Accept any city from the user and display monument of that city.
#                   City        Monument
#                   Delhi       Red Fort
#                   Agra        Taj Mahal
#                   Jaipur      Jal Mahal
city=str(input("Enter any city"))
if "Delhi"==city:
    print("Red Fort")
elif "Agra"==city:
    print("Taj Mahal")
elif "Jaipur"==city:
    print("Jal Mahal")
else:
    print("The city does not exist")

                        
# Q8. Write the output of the following:
a = 9
        
if (a > 5 and a <=10):    
         print("Hello")    
else:    
        print("Bye")

# Q9. Write a program to check whether a person is eligible for voting or not. (accept age from user)
age=int(input("Enter eligible number"))
if age>=21:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

# Q10. Write a program to check whether a number entered
#  by user is even or odd.
x=int(input("Enter number"))
if x%2==0:
    print("odd")
else:
    print("even")
# Q11. Write a program to check whether a number is divisible by 7 or not.
x=int(input("Enter number"))
if x%2==0:
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")

# Q12. Write a program to display "Hello" if a number entered by user is a multiple of five , 
# otherwise print "Bye".
x=int(input("enter a number"))
if x%5==0:
    print("Hello")
else:
    print("Bye")

# Q13. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
x=int(input("enter a number"))
if x==100:
    print("no charge")
elif x>=100:
    print("Rs 5 per unit")
elif x==200:
    print("Rs 10 per unit")
else:
    print("Rs 2000")

# Q14. Write a program to display the last digit of a number.
# (hint : any number % 10 will return the last digit)
x=int(input("enter number"))
print("last digit is", x%10)

# Q15. Write a program to check whether the last digit of a number
# ( entered by user ) is  divisible by 3 or not.
x=int(input("enter number"))
if x%3==0:
    print("true")

