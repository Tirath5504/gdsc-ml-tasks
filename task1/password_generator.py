# Task 1.1 from GDSC - ML TASKS
# Make a random password generator


import random
import string


def intro():

    print("Hello! Welcome to my Random Password Generator!")
    print("Customize your random password by selecting from the following choices: ")
    print("(Click 'y' for YES and 'n' for NO)")


def correct_choice(input):

    if input != 'y' and input != 'n':
        return False
    else:
        return True


def choices():

    flags = [0, 0, 0, 0]

    choice = [
        (0, "small alphabets"),
        (1, "large alphabets"),
        (2, "digits"),
        (3, "special characters"),
    ]
            
    ans = []

    while not all(flags):

        for (index, text) in choice:

            if flags[index] != 1:

                response = input(f"Should random password contain {text}? ")

                if correct_choice(response):
                
                    flags[index] = 1
                    ans.append(response)
                    break
            
                else:

                    print("Invalid Choice")
    
    return ans


def correct_length(length):

    try:

        int(length)
        return True

    except ValueError:

        return False


def randomly_split_pass(length, count_choice):

    parts = []

    for _ in range(count_choice - 1):

        part = random.randint(1, length - (count_choice - len(parts)))
        parts.append(part)
        length -= part

    parts.append(length)

    return parts


def compute(choice, length):

    count_choice = choice.count('y')

    length_of_each_choice = randomly_split_pass(length, count_choice)

    password = []

    inputs = [string.ascii_letters.lower(), string.ascii_letters.upper(), string.digits, string.punctuation]

    for i in range(count_choice):

        for _ in range(length_of_each_choice[i]):

            password.append(random.choice(inputs[i]))

    random.shuffle(password)
    return password
    

def main():

    intro()

    choice = choices()

    while True:

        length = input("What should the length of the random password be? ")

        if correct_length(length):
            length = int(length)
            break
    
    random_password = compute(choice, length)

    print(f"Randomly generated password: {''.join(random_password)}")
    print("May all your accounts be forever safe!")


if __name__ == "__main__":
    main()