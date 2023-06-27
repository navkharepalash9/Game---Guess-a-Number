import random
print("You will get only 9 occasions to guess correct number\n So ALL THE BEST \n GAME START")
a = int(input("How many digit of number you want to guess :- "))
n = random.randint(10**(a-1),10**a)
No_of_Guesses = 1
while(No_of_Guesses <= 9):
    x=int(input("Enter your guesse number : "))
    if x>n:
        print("Enter the number less than ",x)
       # continue
    elif x<n:
        print("Enter the number greater than ",x)
        #continue
    else:
        print("You Enter Correct Number ")
        print("You took ",No_of_Guesses,"no.s of Guesses")
        break
    print("No.s of guesses left",9-No_of_Guesses )
    No_of_Guesses = No_of_Guesses +1
    if (No_of_Guesses > 9):
        print("Game Over \nCorrect number is ",n ,"\n Do you want to play it again then refresh the page \n Thank you for playing")
