# demonstrates while loop without break

def main():
	userInput = ""
	while userInput != "your name": 		# != means 'is NOT equal to' -> while userInput is not equal to 'your name'
		userInput = input('Type "your name"_')
		if userInput == "your name":	# user typed in 'your name' as instructed!
			print("That is correct!")
			#break 						# break no longer needed. the loop will not run again as userInput is now = 'your name'
		else:								# user typed in their real name
			print(f"{'Unfortunately, that is wrong!'.upper()} Try again...\n") # shout at the user! (UPPER CASE)
			
	input("Press Enter to quit")

main()
