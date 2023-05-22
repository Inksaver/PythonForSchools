# demonstrates str()

def main():
	# create a number variable and give it a value of 10
	myNumber = 10
	# Try and Print out the value of the variable
	#print("the variable myNumber contains: " + myNumber)

	# With Python, this will not work, and you get this message:
	# TypeError: Can't convert 'int' object to str implicitly
	# or can only concatenate str (not "int") to str
	# use str() to be certain
	print("str(myNumber) = " +  str(myNumber))
	
	# even better, use f string (interpolation)
	print(f"myNumber = {myNumber}")

main()

input("Press Enter to quit")