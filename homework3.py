#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#here we set the secret
word = "psychological"

print("Kelime %s karakterden oluşmaktadır" %len(word))
print ("Start guessing...")

#creates an variable with an empty value
guesses = ' '

# make a counter that starts with zero
failed = 0   

wrong=0

guess_list = []

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

turn = len(HANGMAN)

deneme = turn

while wrong < turn :    
   
    failed=0 

    guess = input("guess a character:") 
    
    if guess not in guess_list:
      guess_list.append(guess)

      guesses += guess 
      
      for char in word:      

        if char in guesses:      
          print (char)
        
        else:
            # if not found, print a dash
            print ("_")  
            
            # and increase the failed counter with one
            failed += 1   
        
    else:
      print("You have already entered this guess. Please try another guess!k")
      continue

    if failed == 0 :
       print("Congrats! You won ")
       break

    if guess not in word:  
 
        print("WRONG! Try again!")
        print(HANGMAN[wrong]) 
        
        deneme = deneme - 1
        
        wrong += 1

        print("You have " + str(deneme) + ' more guesses')

if  wrong == len(HANGMAN):          
    print ("UNLUCKY! You lose !")
    