# demonstrates  len, .upper(), .lower(). title()

def main():
	userInput = input("Type your name_")
	# len returns the length of the string inside the brackets as an INTEGER
	numberOfChars = len(userInput)
	print(f"Your name {userInput} has {numberOfChars} characters in it")
	
	# string.upper() converts all characters to UPPER CASE
	print(f"Your name {userInput} in upper case is {userInput.upper()}")
	
	# .lower() converts all characters to lower case
	print(f"Your name {userInput} in lower case is {userInput.lower()}")
	
	# .title() converts all characters to Title Case
	print(f"Your name {userInput} in title case is {userInput.title()}")	

main()

input("Press Enter to quit")
