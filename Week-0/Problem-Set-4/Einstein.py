# Get the mass of the object from the user and convert it to an integer
m = int(input("Enter the mass of the object: "))

# Define the speed of light in meters per second
c = 300000000

# Calculate the energy using Einstein's formula (E = mc²)
e = m * c**2

# Print the calculated energy
print(e)