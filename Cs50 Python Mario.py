from cs50 import get_int
#no negative numbers
#range from 1-8
#Has to be a pyramid and the pyramid right facing

#get input from user until correct
while True:
    n = get_int("Enter Height: ")
    if n > 0 and n < 9:
        break

def get_height():
    for i in range(0, n, 1):
        for j in range(0, n , 1):
            if (i + j < n -1):
                print(" ", end="")
            else:
                print("#", end="")
        print()

get_height()




#You could also write the code like thus below:
#Keep in mind the code above uses the get_int so you need to import that from cs50, if you dont want to then just use int(input()).

while True:
    try:
        n = int(input("Enter Height: "))
        if n >= 1 and n <= 8: 
            break
        elif n <= 0 and n >= 9:
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



