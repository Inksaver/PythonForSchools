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
	name = input_x("what is your name?")
	age = input_x("How old are you?", "int")
	likesPython = input_x("Do you like Python? (y/n)", "bool")
	
	print(f"User {name} is {age} years old")
	print(f"Next year you will be {age + 1} years old")
	if likesPython:
		print(f"{name} likes Python")
	else:
		print(f"{name} does not like Python")

main() # program starts here
input("Press Enter to quit")