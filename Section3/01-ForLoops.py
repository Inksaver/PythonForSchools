# demonstration of for loops and repeat string

def main():
	numberOfRows = input("Type a number between 5 and 20_")
	
	numberOfRows = int(numberOfRows)
	if numberOfRows > 1:
		
		# draw a triangle
		# for variable = start, finish, step do
		for i in range(numberOfRows): # eg start at 1 step to 6: 1, 2, 3, 4, 5, 6
			# i starts at 0, then steps 1, 2, 3, 4, 5, etc -> numberOfRows
			lineOfChars = "*" * i # multiply string by i (Can be used for >1 character)
			print(lineOfChars)
		# reverse the triangle by starting with a high number and using -1 for the step: 6, 5, 4, 3, 2, 1
		for i in range(numberOfRows, 0, -1):
			# alternative repeat characters
			lineOfChars = "".ljust(i, "*") # -> left justify an empty string to length i using "*"
			print(lineOfChars)
			
	input("Press Enter to quit")

main() # program starts here

