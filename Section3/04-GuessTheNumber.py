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
	n = random.randint(1, 99)	# pick a number between 1 and 99

	guess = -1
	while guess != n:
		# no need to convert guess to a number, as return type is guaranteed
		guess = input_x("Enter an integer from 1 to 99", "int")
		if guess < n:
			print("Too low")
		elif guess > n:
			print("Too high")
		else:
			print("you guessed it!")
			
	input("Press Enter to quit")

main()