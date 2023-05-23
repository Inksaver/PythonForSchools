import random

def input_x(prompt, dataType = "string"): 	# get input from user
	# if not supplied then give default value
	while True:						# break not required as return used instead
		userInput = input(prompt+ "_")
		if dataType == "string":
			return userInput
		elif dataType == "int":
			try:
				return int(userInput)
			except:
				print(f"Enter a number {userInput} does not work")
		elif dataType == "float":
			try:
				return float(userInput)
			except:
				print(f"Enter a number {userInput} does not work")		
		elif dataType == "bool":
			if userInput.lower()[0] == "y":
				return True
			elif userInput.lower()[0] == "n":
				return False
			else:
				print(f"Enter y or n {userInput} does not work")

def main():
	n = random.randint(1, 99)
	closestAbove = 99
	closestBelow = 1
	guess = -1
	while guess != n:
		guess = input_x(f"Guess the number (between {closestBelow} and {closestAbove})", "int")
		if guess < n:
			if guess > closestBelow:
				closestBelow = guess
			print(f"guess is low. (Between {closestBelow} and {closestAbove})")
		elif guess > n:
			if guess < closestAbove:
				closestAbove = guess
			print(f"guess is high. (Between {closestBelow} and {closestAbove})")

	print("you guessed it!")
	
	input("Press Enter to quit")

# program runs from here
main()