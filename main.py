#program to check if user input numbersare equal without using any comparision operator
def check_if_same(number1, number2):
    #use XOR operator as a ^ a is always 0
    if ((number1 ^ number2) != 0):
        print("NUMBERS ARE NOT EQUAL!!!")
    else:
        print("BOTH NUMBERS ARE EQUAL!!!...")
#taking input 
number1 = int(input("ENTER YOUR FIRST NUMBER..."))
number2 = int(input("ENTER YOUR SECOND NUMBER..."))
check_if_same(number1, number2)