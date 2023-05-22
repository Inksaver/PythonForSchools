# demonstrate float and use of tostring() and tonumber()

def main():
	# Float variables
	myFloat  = 1.5 # create a float variable
	# Note the use of the tostring() function
	print("The variable myFloat contains: " + str(myFloat))
	
	# get a number from the user
	userInput = input("Type a number from 1 to 100 (program will crash if not a number)_")
	# convert userInput to number
	userInput = float(userInput) # if it cannot be converted it errors

	# ValueError: could not convert string to float:
	print("Your number: " + str(userInput) + " multiplied by " + str(myFloat) + " = " + str(userInput * myFloat))
	# or use f string
	print(f"Your number: {userInput} multiplied by {myFloat} = {userInput * myFloat}")

main()

input("Press Enter to quit")