# demonstrate if statement to prevent crash

def main():
	# Float variables
	myFloat  = 1.5 # create a float variable
	# Note the use of the str() function
	print("The variable myFloat contains: " + str(myFloat))
	
	# get a number from the user
	userInput = input("Type a number from 1 to 100_")
	# convert userInput to number
	try:
		userInput = float(userInput) # if it cannot be converted it errors
		print(f"Your number: {userInput} multiplied by {myFloat} = {userInput * myFloat}")
	except:
		print("You did not type a number")
		
main()

input("Press Enter to quit")