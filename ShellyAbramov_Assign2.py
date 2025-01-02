#Shelly Abramov
#Assignment 2
#9/20/2024
#Description: I am designing a program using problem solving, and control structures such as loops and if/else statements leading to input/outputs.

def main():
    # a)
    print("How long has it been since the start of the freezer power failure in whole hours and minutes?")
    response_hours = int(input())
    response_minutes = int(input())     
    if response_hours >=0 and response_minutes >= 0:
        print (f'{response_hours} hours ' f'{response_minutes} minutes')
    else:
        print("Invalid, try a nonnegative integer.")

    #How do I make a space in between the hours and minutes, instead of having the user put the hours and minutes seperate?
    #####################################

    #b)
    hours = response_hours+response_minutes/60
    print(f'{hours:.2f} hours')
      
    ###################################
    #c)
    
    if hours > 16:
        hours = 16
        temperature_celcius = ((4*(hours**2))/(hours+2))-20
        print("The freezer is warm enough to be in room temperature." f' {temperature_celcius:.2f} degrees celcius')     
    else:
        temperature_celcius = ((4*(hours**2))/(hours+2))-20
        print(f'{temperature_celcius:.2f} degrees celcius')
    
##    if hours <=16:
##        print(f'{temperature_celcius:.2f} degrees celcius')
##    else:
##        print("The freezer is warm enough to be in room temperature.")

    #########################################
        
    #d)
    farenheit = (temperature_celcius*(9/5))+32
    print(f'{farenheit:.2f} degrees farenheit')
    # is that ok that I am rounding it to 2 decimal places if it didn't require me to
    #######################################
    
    #e)
    print(f'{temperature_celcius:.1f} degrees celcius and ' f'{farenheit:.1f} degrees farenheit' +  f' {hours:.2f} hours after power failure.')
    ############################################
    
    #f)
    if temperature_celcius >= -10: 
        print("Ice cream is spoiled.")
    else:
        print("Ice cream is not spoiled.")
    ##############################################
    #g)
    if farenheit >=40 or temperature_celcius >=4.5:
        print("Please discard your meat and poultry products, they are spoiled.")
    else:
        print("Your meat and poultry products are not spoiled yet, no need to discard.")
    print("\n")
#########################################
    #h)
    repeat_loop = input("Hello again, is your power back? Yes or No ")
    if repeat_loop == "No":
        main()
    elif repeat_loop == "Yes":
        print("That's great to hear!")
    else:
        print("That is not a valid entry, please input Yes or No.")
   
main()


    


