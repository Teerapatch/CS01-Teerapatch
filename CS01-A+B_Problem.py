A = int(input("Input your number1 : "))
B = int(input("Input your number2 : "))

if A < 0 :
    print("Error! your number1 is under 0")
    A = int(input("Input your number : "))
elif A > 10**9 :
    print("Error! your number1 is higher 10**9")
    A = int(input("Input your number : "))
elif B < 0 :
    print("Error! your number2 is under 0")
    B = int(input("Input your number : "))
elif B > 10**9 :
    print("Error! your number2 is higher 10**9")
    B = int(input("Input your number : "))

print("Your result is :",A+B)