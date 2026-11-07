# Gets input from the user
text = input("Hello ")

# Checks if the input starts with "hello"
if text.startswith("hello"):
    print("$0")  # Prints $0 if the input starts with hello

# Checks if the input starts with "h"
elif text.startswith("h"):
    print("$20")  # Prints $20 if the input starts with h

# If neither condition is true
else:
    print("$100")  # Prints $100 if the input starts with anything else