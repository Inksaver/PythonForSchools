# int(), str()

def main():
	# Anything typed in is a string, INCLUDING numbers!
	# Ask the user to type something, and store what they typed.
	userInput = input("Type in any letters, numbers or symbols and press Enter")
	print("You typed in the characters " + userInput)
	# Ask the user to enter only numbers
	userInput = input("Type in any number, and press Enter")

	# If they typed in 3, it is the character "3"
	# You have to convert it to a number
	userInput = int(userInput) # if it cannot be converted it errors
	# ValueError: invalid literal for int() with base 10
	print("The variable userInput now contains:  " + str(userInput))

main()

input("Press Enter to quit")