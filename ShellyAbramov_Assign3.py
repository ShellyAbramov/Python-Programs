#Shelly Abramov
#Assignment 3
#10/5/2024
#Description: I am creating user-defined functions, lists, random number generators, loops, and functional programming

#1. Lottery Number Generator

def lottery(random):
    """Generates 6 random unique lottery numbers"""
    import random
    winning_random_list=[]
    for i in range(6):
        winning_num = random.randint(1,49)
        winning_random_list.append(winning_num)
    return winning_random_list
      
###########################################################################################     

#2 Rainfall Statistics
def rainfall_stats(rainfall):
    """Calculates and displays total, average, and max/min monthes of rainfall"""
    #To find the sum. 
    total_rainfall = sum(rainfall)
    #finds the average
    average=total_rainfall/len(rainfall)
    #finds the max and min
    max_rainfall= max(rainfall)
    min_rainfall= min(rainfall)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'
              'September', 'October', 'November', 'December']
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]
    
    #Displays the results to the user
    print('Total annual rainfall is ' f'{total_rainfall:.2f} inches')
    print(f'Average monthly rainfall is {average:.2f} inches')
    print(f'Month with highest rainfall is {max_month} with {max_rainfall:.2f} inches')
    print(f'Month with the lowest rainfall is {min_month} with {min_rainfall:.2f} inches')  

###############################################################################################
#3 Driver's License Exam

def drivers_exam(student_answers):
    '''This function grades the person by storing input and comparing it to the answers, then determining how many right they got out of total'''

    #stores the correct answers in a list
    correct_answers = ['B', 'D', 'A', 'A','C', 
                       'A', 'B', 'A', 'C', 'D', 
                       'B', 'C', 'D', 'A', 'D', 
                       'C', 'C', 'B', 'D', 'A']

    #  counters and lists
    correct_count = 0
    incorrect_questions = []

    # Compare student answers with correct answers
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            correct_count += 1 #counts the amount of right questions answered
        else:
            incorrect_questions.append(i + 1)  #adds wrongs questions to a list
    # Determine pass/fail status
    passed = correct_count >= 15 #will return yes or no type

    # Return results
    return passed, len(incorrect_questions), incorrect_questions
#can also make it happen with a list comprehension

######################################################################################################
#4 Expense Pie Chart
import matplotlib.pyplot as plt

def user_expenses():
    """This function helps create a pie chart given the expenses of a user"""
    # expense categories
    categories = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment/Commute', 'Entertainment']
    expenses = []
    

    print("Please enter your expenses from the past month for the following categories:")
    for category in categories:
        while True:  # Loop until valid input is provided
            try:
                amount = float(input(f'{category}: '))
                expenses.append(amount)  # Appends or adds the the amount to the expenses list
                break  # will exit the loop if input is valid
            except ValueError:
                print('Invalid input, please enter a numeric value.')

    # Plots the expenses
    plt.pie(expenses, labels=categories, autopct='%1.1f%%')
    plt.title("Recent Monthly Expenses")
    plt.show()
    #I put return but it was giving me error, so I removed it, why is return not needed?

#############################################################################################################
#5 Lo Shu Magic Square

def lo_shu_magic_square(square):
    rows = 3
    cols = 3
    for r in range(rows):
        for c in range(cols):
            while True:
                try:
                    value =int(input("Please enter a value between 1 - 9 for the row " + str(r+1) + ' and ' + 'column ' +str(c+1) +': '))
                    if value in range(1,10) and value not in [num for row in square for num in row]: #values cannot repeat, that's why made a list comprehension
                        square[r][c] = value
                        break
                    else:
                        print('Please input a number between 1 and 9 that has not been repeated.')
                except ValueError:
                    print('Please input a valid number between 1 and 9.')
            
    return square

#################################################################################################################
def main():
    #1 Lottery Number Generator

    import random
    print('Please enter your 6-digit lottery number, with each value between 1 and 49.')
    user_input_list=[]    
    user_input1=int(input())
    user_input2=int(input())
    user_input3=int(input())
    user_input4=int(input())
    user_input5=int(input())
    user_input6=int(input())
    user_input_list.append(user_input1)
    user_input_list.append(user_input2)
    user_input_list.append(user_input3)
    user_input_list.append(user_input4)
    user_input_list.append(user_input5)
    user_input_list.append(user_input6)
    print('Your input' f'{user_input_list}')
    print("Winning numbers" f'{lottery(random)}')

    if user_input_list == lottery(random):
        print("You are a WINNER!")
    else:
        print('Sorry, you are not a winner.')

        print('\n')
###########################################################################################

    #2 Rainfall Statistics
        birth_city_rainfall_miami = [1.62, 2.25, 3.00, 3.14, 5.34, 9.67,
                                6.50, 8.88, 9.86, 6.33, 3.27, 2.04]
        rainfall_stats(birth_city_rainfall_miami)
        print('\n')
############################################################################################
    #3 Driver's License Exam
    student_answers = []
    print("Please enter your answers for the 20 question Driver's License Exam.")

    for i in range(1, 21):
        answer = input(f"Question {i}: ").strip().upper()  
        while answer not in ['A', 'B', 'C', 'D']:  # Validates input
            print("Invalid. Please enter A, B, C, or D.")
            answer = input(f"Question {i}: ").strip().upper() #like learned in ch.7 upper helps make the letters uppercase
                                                                #if input was lowercase to match correct answers and string removes the spaces. 
        student_answers.append(answer)

    # Grades the exam
    passed, incorrect_count, incorrect_questions = drivers_exam(student_answers)

    # Displays and shows the results
    if passed:
        print("Congrats! You passed the exam.")
    else:
        print("Sorry unfortunately, you failed the exam.")
        
    print(f"You answered {len(student_answers) - incorrect_count} questions correctly.")
    print(f"You answered {incorrect_count} questions incorrectly.")
    if incorrect_count > 0:
        print("Questions answered incorrectly were ",incorrect_questions)
        print('\n')
#####################################################################################################
        #4 Expense Pie Chart

    # Call the function to get user expenses and plot the pie chart
    user_expenses()
    
    #print('\n')
##############################################################################################
    #5 Lo Shu Magic Square
    rows = 3
    cols = 3
    lo_shu_magic_square_list = [[0,0,0],
                                [0,0,0],
                                [0,0,0]] #or am i supposed to make this empty lists
    #creates a variable which calls the function and then inputs the empty list that can be altered
    magic_list = lo_shu_magic_square(lo_shu_magic_square_list)
    
    #calculate sum of rows
    #the numbers next to magic list are the indexes of the rows and colms to determine the position and add it up
    #row and col starts and with 0 
    sum_row1 = magic_list[0][0] + magic_list[0][1] + magic_list[0][2]
    sum_row2 = magic_list[1][0] + magic_list[1][1] + magic_list[1][2]
    sum_row3 = magic_list[2][0] + magic_list[2][1] + magic_list[2][2] #I can also use list comprehensions

    #calculate sum of cols
    #adds the values in the indexes that the user input
    sum_col1 = magic_list[0][0] + magic_list[1][0] + magic_list[2][0]
    sum_col2 = magic_list[0][1] + magic_list[1][1] + magic_list[2][1]
    sum_col3 = magic_list[0][2] + magic_list[1][2] + magic_list[2][2]

    #calculate sum of diagonals
    sum_diag1 = magic_list[0][0] + magic_list[1][1] + magic_list[2][2]
    sum_diag2 = magic_list[0][2] + magic_list[1][1] + magic_list[2][0]

    for i in range(3):
        for j in range(3):
            print(magic_list[i][j], end = ' ')
        print("\n")

    if sum_row1 == sum_row2 == sum_row3 == sum_col1 == sum_col2 == sum_col3 == sum_diag1 ==  sum_diag2:
        print("The square is a Lo Shu Magic Square.")
    else:
        print("The square is NOT a Lo Shu Magic Square.")

               
if __name__ == '__main__':
    main()
            
            
    
    
    
    




