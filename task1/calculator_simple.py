# Task 1.2 of GDSC - ML Tasks
# WAP that implements a simple calculator


import math

def main():

    print("Welcome to my calculator program!")
    print("Enter 'q' to exit")

    while True:

        try:

            result = eval(input("Enter an expression: "), {"__builtins__": {}}, {})
            
            if result == float("inf"):
                print("Error: Division by zero")
            else:
                print("Result:", result)

        except Exception:
            print("Sayonara!")
            break


if __name__ == "__main__":
    main()
    