#Name: Shelly Abramov
#Assignment 4
#11/6/2024
#Description: I am working with All built-in data structures (dictionary, set, string) , File processing

#1 Capital Quiz
##print("1. Capital Quiz")
import random
def capital_quiz():
    state_capital_dict={} #This empty dictionary will help put the file, into a dictionary
    
    with open('US_States.txt', 'r') as file: #This opens the text file
        #line = file.readlines() #This reads the text as a list of lines


        for line in file: #For loop will iterate through each line
            state_capital = line.strip().split('\t')
            state = state_capital[0] #this is the key #used indexing
            capital = state_capital[1] #this is the value 
            state_capital_dict[state] = capital #this adds a new key value pair
        return state_capital_dict
   
    #print(state_capital_dict) #This was used for debugging

def user_answers(state_capital_dict):
    correct_count = 0
    incorrect_count = 0
    asked_states = set() #this empty set will help keep track of asked states to not repeat

    #Below keeps track of correct and incorrect answers
    while True: #makes the loop to iterate over many states
        if len(asked_states)== len(state_capital_dict):
            print("All the states have been answered! The quiz is finished.")
            break #This exits the loop if all the sames have been asked
        
        remaining_states = list(state_capital_dict.keys()- asked_states)#list makes it into a list, and .keys takes all keys in the dict, additonially this uses the set difference operation -
        random_state = random.choice(remaining_states) #chooses a random state from the list of remaining states only 
        asked_states.add(random_state) # this marks the state as asked and puts in into that set

        #Below asks the user for capital of state
        print(random_state)
        user_input = input(f'What is the capital of {random_state}? ').strip()
        correct_answer = state_capital_dict[random_state]
        
        if user_input == correct_answer or user_input == correct_answer.lower():
            print("CORRECT!")
            correct_count +=1
        else:
            print(f"INCORRECT! The correct answer is {correct_answer}.")
            incorrect_count +=1

        continue_quiz = input("Do you want to continue? Yes or No: ").strip().lower()
        if continue_quiz != "yes":
            break
    print(f"The quiz is finished. You got {correct_count} correct and {incorrect_count} incorrect.")
    
   #print(correct_count, incorrect_count)#This was used for debugging    
    
##state_capital_dict = capital_quiz()#setting up the parameter and then setting it equal to the call function
##user_answers(state_capital_dict)


#2: File Encryption and Decryption
##print("2.File Encryption and Decryption")

def file_encryption():
    codes_dict = {'A': '%','a':'9', 'B':'@', 'b':'#', 'C':'!', 'c':'$', 'D':'&', 'd':'a','E':'s','e':'q','F':'y','f':'t','G':'x','g':'u','H':'p','h':'o',
                  'I':'c','i':'v','J':'w','j':'1','K':'2','k':'3','L':'4','l':'5','M':'6','m':'7','N':'0','n':'8','O':'z','o':'r','P':'E','p':'A','Q':'B',
                  'q':'d','R':'C','r':'h','S':'K','s':'l','T':'G','t':'Q','U':'M','u':'f','V':'p','v':'T','W':'L','w':'j','X':'i','x':'b','Y':'W','y':'n',
                  'Z':'?','z':'M'}
    with open('RomeoJuliet-1.txt','r') as file1, open('encryption.txt','w') as file2:
        for line in file1:
            encrypted_line = '' #makes an empty string
            for character in line:
                encrypted_line += codes_dict.get(character, character) #append the value to the key in the code.
            file2.write(encrypted_line) #this writes the encrypted line into the file2 (encryption.txt)
    print("Complete! File RomeoJuliet-1.txt has been encrypted.") #used for debugging
    #Below will print the encrypted version of Romeo and Juliet
    with open ('encryption.txt','r') as file2:
        file_contents = file2.read()
        print(file_contents)

##file_encryption()

def file_decryption():
    codes_dict = {'A': '%','a':'9', 'B':'@', 'b':'#', 'C':'!', 'c':'$', 'D':'&', 'd':'a','E':'s','e':'q','F':'y','f':'t','G':'x','g':'u',
                  'H':'p','h':'o','I':'c','i':'v','J':'w','j':'1','K':'2','k':'3','L':'4','l':'5','M':'6','m':'7','N':'0','n':'8','O':'z',
                  'o':'r','P':'E','p':'A','Q':'B','q':'d','R':'C','r':'h','S':'K','s':'l','T':'G','t':'Q','U':'M','u':'f','V':'p','v':'T',
                  'W':'L','w':'j','X':'i','x':'b','Y':'W','y':'n','Z':'?','z':'M'}
    #use dictonary comprehension to reverse the values and keys
    reverse_codes_dict = {v:k for k, v in codes_dict.items()}
    
    with open('encryption.txt','r') as file1, open('decryption.txt','w') as file2:
        for line in file1:
            decrypted_line = '' #make an empty string to concatenate later
            for character in line:
                decrypted_line += reverse_codes_dict.get(character, character)

            file2.write(decrypted_line) #writes the decrypted lines into the other file
    print("Complete! The encrypted file has been decrypted.")
    with open('decryption.txt','r') as file2:
        file_contents = file2.read()
        print(file_contents)

##file_decryption()

        
#3 Average Number of Words
##print("3. Average Number of Words")

def calculate_average_words():

#####do we need a dictionary for this or can we save it as a list and make it work?
    with open('RomeoJuliet-1.txt', 'r') as file:
        words_in_sentences = {line.strip(): len(line.strip().split()) for line in file} #dictionary comprehension
        
        #prints each sentence and its word count using a for loop to iterate through each one
        for sentence, word_count in words_in_sentences.items():
            print(f'{sentence} : {word_count} words')

        if words_in_sentences:
            average_words = sum(words_in_sentences.values())/len(words_in_sentences)
            print(f"The average number of words per sentence is {average_words:.2f} words.")
        else:
            print("There are no sentences in this file.")

##calculate_average_words()


#4 Unique Words
##print('4.Unique Words')

def unique_words_infile():
    unique_words = set()
    with open('RomeoJuliet-1.txt','r') as file:
        for line in file:
            words = line.strip().split() #splits the line into a list of words
            for word in words: #iterates through each word in the list of words
                unique_words.add(word)

    print("Unique words in this file:")
    for word in unique_words:
        print(word)

##unique_words_infile()
                        
        
def main():
###1
    print("1. Capital Quiz")
    print('')
    state_capital_dict = capital_quiz()#setting up the parameter and then setting it equal to the call function
    user_answers(state_capital_dict)
    print('')
    print('')
    ########################################
###2
    print("2.File Encryption and Decryption")
    print('')
    file_encryption()
    print('')
    print('')
    file_decryption()
    print('')
    print('')
    ##########################################
###3
    print("3. Average Number of Words")
    print('')
    calculate_average_words()
    print('')
    print('')
##4
    print('4.Unique Words')
    print('')
    unique_words_infile()

if __name__ == "__main__":
    main()

    
    
    
    

    

    
    



                
