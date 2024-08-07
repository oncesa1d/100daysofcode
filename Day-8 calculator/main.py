from modules import logo

print(logo)


def calculator():
    print("Welcome to my super puper calculator!")
    operation = int(input('Which operation do you want? \n (1) = "+" , (2) = "-" , (3) = "*" , (4) = "/" \n'))
    first_number = float(input('Write first number: \n'))
    second_number = float(input('Write second number: \n'))

    if operation == 1:
        result = first_number + second_number
    elif operation == 2:
        result = first_number - second_number
    elif operation == 3:
        result = first_number * second_number
    elif operation == 4:
        result = first_number / second_number
    else:
        print("Error! Please Please enter a number.")
        return

    print(f"Result is {result}")


calculator()
    
