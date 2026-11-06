# Get text from the user
def main():
# Convert emoticons to emojis and display the result
    text = input("Enter somthing: ")
    print(convert(text))
def convert(text):
# Replace happy and sad emoticons with emojis
    return text.replace(":)","🙂").replace(":(","☹️")
# Run the main function

main()