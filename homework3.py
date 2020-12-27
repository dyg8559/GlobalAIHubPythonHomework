#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#here we set the secret
word = "psychological"

print("Kelime %s karakterden oluşmaktadır" %len(word))
print ("Start guessing...")

#creates an variable with an empty value
guesses = ' '

#determine the number of turns
turns = len(word) - 1

# make a counter that starts with zero
failed = 0   

wrong=0


HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

while turns > 0  : 

    failed=0

    guess = input("guess a character:") 
    
    guesses += guess  
           
    for char in word:      

        if char in guesses:      
            print (char)
        
        else:
            # if not found, print a dash
            print ("_")     
       
            # and increase the failed counter with one
            failed += 1   

    if failed == 0 :
       print("Congrats! You won ")
       break

    if guess not in word:  
 
        turns -= 1        
        wrong += 1

        print("WRONG! Try again!")
        print(HANGMAN[wrong]) 

        if turns == 0 :          
    
            print ("UNLUCKY! You lose !")

        else:

            print("You have " + str(turns) + ' more guesses')



