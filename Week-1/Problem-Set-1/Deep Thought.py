# Takes input from the user
text = input("Enter something: ")

# Checks if the input is equal to 42 in any of these formats
if text == "42" or text == "forty two" or text == "forty-two":
    print("Yes")  # Prints Yes if the condition is true
else:
    print("No")   # Prints No if the condition is false