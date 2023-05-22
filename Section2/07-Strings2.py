
def main():
	userInput = input('Type "your name"_')

	if userInput == "your name":	# user typed in 'your name' as instructed!
		print("That is correct!")
	else:	# user typed in their real name
		# use of f string with upper(), lower() or title() by using single quotes
		print(f"{'Unfortunately, that is wrong!'.upper()} Try again...\n") # shout at the user! (UPPER CASE)

main()

input("Press Enter to quit")