# Problem Statement
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

# Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk,
#  and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# If the user enters anything else we print out:

# Sorry I only tell jokes

PROMPT= "what do you want?"

Joke= "Patient: will I be able to play the piano after the operation? nurse: Sure of course!, Patient:That's awesome beacause I couldn't before."

def joke():

    user_input = input(PROMPT)
    
    if user_input.lower() == "joke":
         print(Joke)

    else:
        print("Sorry I only tell jokes")

if __name__ == '__main__':

    joke()
