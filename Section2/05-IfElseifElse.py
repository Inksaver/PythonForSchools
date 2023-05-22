# demonstrates boolean variables and if elif else
def main():
	# Boolean variables can only be either true or false
	# Most languages associate true = 1, false = 0
	# You can also think of yes = true, no = false
	
	choice = False # variable called 'choice' is given the default value False
	userInput = input("Do you like Python? (y/n)_")
	# user SHOULD have typed a 'y' or 'n'
	if userInput == "":					# Enter only
		print("You only pressed the Enter key")
	elif userInput == 'y':				# 'y' typed in
		print("Great! variable 'choice' is now True")
		choice = True			# set choice to true as the user typed 'y'
	elif userInput == 'n':				# 'n' typed in
		print("Oh. That is disappointing")
	else:								# some other characters typed in
		print(f"You typed {userInput} I can't translate that to True/False")
	
	print(f"\nThe value of the boolean variable 'choice' is: {choice}")

main()

input("Press Enter to quit")