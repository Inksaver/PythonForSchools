# demonstrates use of the while loop
'''
 In the previous script, it only runs once. If you type in the
 words "your name" you get a brownie point. Otherwise you are wrong.
 But you can only do it once, then you have to re-start.
 Use a loop to allow another chance:
'''

def main():
	while True: # True is always True, so this is an infinite loop
		userInput = input('Type "your name"_')
		if userInput == "your name":	# user typed in 'your name' as instructed!
			print("That is correct!")
			break 							# break out of the loop
		else:								# user typed in their real name
			print(f"{'Unfortunately, that is wrong!'.upper()} Try again...\n") # shout at the user! (UPPER CASE)

	input("Press Enter to quit")

main()
