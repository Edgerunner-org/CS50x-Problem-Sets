# Gets a mathematical expression from the user
c = input("What is expression? ")

# Splits the expression into three parts
x, y, z = c.split()

# Checks if the operator is addition
if y == "+":
    result = int(x) + int(z)

# Checks if the operator is subtraction
elif y == "-":
    result = int(x) - int(z)

# Checks if the operator is multiplication
elif y == "*":
    result = int(x) * int(z)

# Checks if the operator is division
elif y == "/":
    result = int(x) / int(z)

# Prints the result with one decimal place
print(f"{result:.1f}")