# Gets the file name from the user
text = input("Enter something: ")

# Checks if the file ends with .gif
if text.endswith(".gif"):
    print("image/gif")

# Checks if the file ends with .jpg
elif text.endswith(".jpg"):
    print("image/jpeg")

# Checks if the file ends with .png
elif text.endswith(".png"):
    print("image/png")

# Checks if the file ends with .txt
elif text.endswith(".txt"):
    print("text/plain")

# Checks if the file ends with .pdf
elif text.endswith(".pdf"):
    print("application/pdf")

# Checks if the file ends with .zip
elif text.endswith(".zip"):
    print("application/zip")

# Checks if the file ends with .jpeg
elif text.endswith(".jpeg"):
    print("image/jpeg")
    
# Prints a default type if the extension is not recognized
else:
    print("application/octet-stream")