#import modules
import sys
import random


#initial variables
questions = True

#list of responses variable
response = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT, YES", "OUTLOOK LOOKS GOOD", "MOST LIKELY", "IT IS DECIDEDLY SO", "WITHOUT A DOUBT", "YES, DEFINITELY"]

#while loop
while questions:
    print("Ask away! (press the ENTER key to exit the app)")
    #user input
    user_input = input()        
    #return the random response
    random_response = response[random.randint(0,7)]
#quit the application if there is no question or get a response if a question is asked
    if user_input == "":
        sys.exit()
    else:
        print(random_response)

    
