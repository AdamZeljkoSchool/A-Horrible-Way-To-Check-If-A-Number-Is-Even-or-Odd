import aHorribleWayToCheckIfANumberIsEvenOrOdd as b
import aGoodWayToCheckIfANumberIsEvenOrOdd as g
choice = str(input("Would you like a good way to check if a number is even or odd or a bad way? [Good/Bad]: "))
if choice == "Good":
    while True:
        number = g.goodOddOrEven(int(input("Input a number: ")))
        print(number)
elif choice == "Bad":
    while True:
        number = b.oddoOrEven(int(input("Input a number: ")))
        print(number)
else:
    print("Invalid choice!")