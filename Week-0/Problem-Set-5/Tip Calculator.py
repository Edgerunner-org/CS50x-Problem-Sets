def main():
    # Get the meal price and tip percentage from the user
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate the tip
    tip = dollars * percent

    # Print the tip amount with two decimal places
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    # Remove the dollar sign and convert the string to a float
    return float(dollars.replace("$", ""))


def percent_to_float(percent):
    # Remove the percentage sign and convert the percentage to a decimal
    return float(percent.replace("%", "")) / 100


# Call the main function
main()