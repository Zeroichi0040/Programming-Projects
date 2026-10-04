print("Please enter 2 values:")
value1 = int(input("Value 1: "))
value2 = int(input("Value 2: "))
operator = input("Please choose an operation(+, -, *, /): ")
if operator == "+":
    print(f"{value1} + {value2} = {value1 + value2}")
elif operator == "-":
    print(f"{value1} - {value2} = {value1 - value2}")
elif operator == "*":
    print(f"{value1} * {value2} = {value1 * value2}")
elif operator == "/":
    print(f"{value1} / {value2} = {value1 / value2}")
