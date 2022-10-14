from cs50 import get_int
#no negative numbers
#range from 1-8
#Has to be a pyramid and the pyramid right facing

#get input from user.
while True:
    n = get_int("Enter Height: ")
    if n >= 1 or n <= 8:
        break
        
def get_height():
    for i in range(n):
        for s in range(n - i - 1, 0 , -1):
            print(" ", end="")
        for hash in range(i + 1):
            print("#", end="")
        print()

get_height()




#YOU COULD ALSO WRITE THE CODE AS THUS BUT IT IS A LOT MORE INFORMATION AND int(input("Height: ")) is not accepted for the cs50 check BUT it seemed to be correct code.
# Or i should say it does take the input and gives a correct output: But go for the top code for this problem.

#get input from user:
while True:
    try:
        n = int(input("Enter Height: "))
        if n >= 1 or n <= 8:
            break
        elif n <= 0 or n >= 9:
            print("Please enter a number from 1 to 8!")
    except ValueError:
            print("Please enter a number!")

def get_height():
    for i in range(n):
        for s in range(n - i - 1, 0 , -1):
            print(" ", end="")
        for hash in range(i + 1):
            print("#", end="")
        print()

get_height()



