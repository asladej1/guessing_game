#looking to qualify for "exceeds expectations" grade. 


import random
GREETING = "======> Welcome to Rando <====="

print(GREETING.upper())


rules = print("Rules: \n******Select a integer between 1 & 10, and I will tell you if it's too high or too low.******")


hi_score = []

def start_game():
    answer = random.randint(1,10)
    num_of_guess = 0

    while answer > 0:
        try:
            guess = int(input("Pick an integer between 1 & 10:  "))
            num_of_guess += 1

        except ValueError as err:
            print(("Whoops, not a valid entry.Please try again using an Integer"))
            continue


        if 1<= guess <= 10:

            if guess == answer:
                print("Congrats! You guessed my number. It took you {} tries".format(num_of_guess))
                replay = input('Would you like to play again?  ')
            
                if replay.lower()== "yes":
                    current_hi_score(num_of_guess)
                    start_game()
    
                else:
                    print("Thanks for playing, comeback again!")
                    exit()

            else:
                if guess > answer:
                    print("It's lower")
                else:
                    print("It's higher")

        else:
            print("Number has to be integer between 1 & 10, try again!")
            
def current_hi_score(num_of_guess):
    hi_score.append(num_of_guess)
    print('Score to beat is {}! Good Luck '.format(min(hi_score)))
    
            
            


start_game()     
  
    
