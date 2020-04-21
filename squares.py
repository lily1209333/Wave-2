pos = str(input("enter a position: "))
letter = pos[0]
number = pos[1]
let1 = ["a", "c", "e", "g"]
let2 = ["b", "d", "f", "h"]
num1 = ["1", "3", "5", "7"]
num2 = ["2", "4", "6", "8"]

if letter in let1:
    if number in num1:
        print("black")
    elif number in num2:
        print("white")
elif letter in let2:
    if number in num1:
        print("white")
    elif number in num2:
        print("black")
