#Shelly Abramov
#9/3/2024
#Assignment_1
#Description: I am learning in/out sequential programming

#### Problem 001 ######
print("Problem 001")
print("\"Grit is that 'extra something' that \n seperates the most successful people \n from the rest. It's the passion, \n",
      "perseverance, and stamina that we \n must channel in order to stick with our \n dreams until they become a reality.\"")
print( "\t-Travis Bradberry\n")

#################################################

##### Problem 002 #####
print("Problem 002")
#inputs : what are the givens?
#ouputs:what should my code calculate and display?

print ("How many days?")
user_response = int(input())
hours_per_day = 24
mins_per_hour = 60 #all lowercase letters, and _ if needed
seconds_per_hour = 60
total_seconds_in_day = user_response*hours_per_day*mins_per_hour*seconds_per_hour
print(f'Seconds in that many days: {total_seconds_in_day:.2f}\n')


#####################################################
#### Problem 003 #####
print("Problem 003")

x = int(input())
y = int(input())
if y == 0:
    print('Error, please select another integer value that is nonzero.\n')
#How do I get this to allow the user to answer this if they get this message
#because it just moves to the next line of code/problem
elif y >=0 or y <=0:
    print(f'{x}+{y} = {x + y:.2f}')
    print(f'{x}-{y} = {x - y:.2f}')
    print(f'{x}*{y} = {x*y:.2f}')
    print(f'{x}/{y} = {x/y:.2f}\n')

#I put that an error comes up when divided by 0. If, else statment.

###########################################################################
#### Problem 004 #####
print('Problem 004')
print("What is your name?")
user_name = str(input())
if user_name.isnumeric():
    print("You entered a number. Please enter a valid name.")
else:
    print(f"In what year were you born?\n")
 
user_year = int(input())
x = 2024 - user_year #the year the user will be by the end of 2024
print (f'Hi {user_name}, you will be {x} years old at the end of year 2024.\n')  

###############################################################################
#### Problem #5 ####
print("Problem 005")
print("How many times a week do you eat at the student cafeteria?")
x = int(input())#times user eats in cafeteria
print("The average of a typical student meal?")
y = float(input())#cost of student meal
print("How much do you spend on groceries in a week?")
z = float(input())#amount on groceries
B = int(7) #days in a week #not a magic number
daily = x*y +(z/B) #I divided the amount spent on groceries by 7 to get the average daily cost in a week
weekly = (B*x*y)+z
print("Average food expidenture:")
print(f'Daily: ${daily:.2f}')
print(f'Weekly: ${weekly:.2f}')

    


