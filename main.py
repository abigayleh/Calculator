def calculate(numb1, numb2, opera):
    if opera.upper() == "A":
        res = float(numb1) + float(numb2)
    elif opera.upper() == "S":
        res = float(numb1) - float(numb2)
    elif opera.upper() == "M":
        res = float(numb1) * float(numb2)
    elif opera.upper() == "D":
        res = float(numb1) / float(numb2)
    return res


def main():
    start = True
    while start:
        num1 = input("Enter a number")
        while not num1.lstrip('-').isnumeric() and num1.lstrip('-').isdecimal():
            num1 = input("Invalid number. Please enter a number")

        op = input("A / S / M / D ")
        while op.upper() != "A" and op.upper() != "S" and op.upper() != "M" and op.upper() != "D":
            op = input("Invalid operator, please enter A,S,M or D")

        num2 = input("Enter another number")
        while not num1.lstrip('-').isnumeric() and num1.lstrip('-').isdecimal():
            num2 = input("Invalid number. Please enter a number")

        result = calculate(num1, num2, op)
        print(result)
        start = False
        store = True

    while store:
        num1 = result
        op = input("A / S / M / D / C")
        while op.upper() != "A" and op.upper() != "S" and op.upper() != "M" and \
                op.upper() != "D" and op.upper() != "C":
            op = input("Invalid operator, please enter A, S, M, D or C")
        if op.upper() == "C":
            start = True
            store = False
            main()
        else:
            num2 = input("Enter another number")
            while not num2.lstrip('-').isnumeric() and num2.lstrip('-').isdecimal():
                num2 = input("Invalid number. Please enter a number")
            result = calculate(num1, num2, op)
            print(result)


main()
