import random
top_range=input("enter the range:")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("please enter greater than 0.")
        quit()
else:
    print("Please enter the range again")
    quit()
random_num=random.randint(0,top_range)
guess=0
while True:
    guess+=1
    user_guess= input("make a guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
   
    else:
        print("Please enter the range again")
        continue
    if user_guess==random_num:
        print("you win")
        break
    elif user_guess>random_num:
        print("you are above the number")
    else:
         print("you are below the number")
        
print("you got it in " +str(guess)+" guesses")