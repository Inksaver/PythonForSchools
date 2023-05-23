
def main():
	numberOfRows = input("Type a number between 5 and 20. (Enter only for 6 rows)")
	if numberOfRows == "":
		numberOfRows = 6
	else:
		numberOfRows = int(numberOfRows)

	for i in range(1, numberOfRows):
		spaces = " " * (numberOfRows - i)			# create a starting string of spaces
		if i == 1:
			lineOfChars = "*" * i
			lineOfChars = f'{spaces}{"*" * i}'			# special case for first line
		else:
			lineOfChars = f"{spaces}{'*' * (i * 2 - 1)}"	# string of * starting with 3, 5, 7, 9, etc
		
		print(lineOfChars)

main() # program starts here

input("Press Enter to quit")