# Task 1.2 of GDSC - ML Tasks
# WAP that implements a complex calculator


import string


def compute(expression):

    operators = ["+", "-", "*", "/"]
    operands = list(string.digits)
    brackets = ["[", "]", "{", "}", "(", ")", "."]
    ans = 0

    flag_operator, flag_operand, exp_count, operator = 0, 0, 0, 0

    for ind, ele in enumerate(expression):

        if ele != " " and ele not in operands and ele not in operators and ele not in brackets:
            print("Invalid Expression")
            break

        if ele == 'c' or ele == 'C':
            ans = 0

        if ele in operators or ele == " ":

            if flag_operator == 0:

                if exp_count == 0:
                    operand1 = expression[ : ind]
                    op1_i = ind
                    flag_operator = 1
                    operator = ele

                else:
                    operand1 = expression[op2_i : ind]
                    op1_i = op2_i
                    flag_operator = 1
                    operator = ele

            elif flag_operator == 1:
                operand2 = expression[op1_i + 1 : ind]
                op2_i = ind
                exp_count += 1
                flag_operator = 0
            
        if flag_operator == 0 and exp_count != 0:
            ans = int(operand1[0]) + operator + int(operand2[0])
            print(ans)


def main():

    while True:

        print("Press q to exit")
        exp = input("Enter a arithmetic expression: ")

        if exp == 'q':
            print("Sayonara!")
            break

        try:
            ans = compute(exp)
            print("Answer: ", ans)

        except Exception as e:
            print("Exception Occurred: ", e)


if __name__ == "__main__":
    main()
