from modules import logo

def add(n1, n2):
    return (n1 + n2)


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    should_accumulate = True
    n1 = float(input("Type the first number: "))
    while should_accumulate:

        for symbols in operations:
            print(symbols)
        operation_symbol = input("Type the mathematical operator: ")
        n2 = float(input("Type the second number: "))
        answer = operations[operation_symbol](n1, n2)

        print(f"Answer is: {n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
