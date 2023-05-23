def get_input(prompt):
	response = input(f"{prompt}>_")

	return response

def quit():
	input("Enter to quit")


# It is good coding practice to use a main() function
def main():
	# assume user is too lazy to use a capital letter
	# use .title() to sort the capital letters out on all words
	print(f"\nYour name (in Caps) is: {get_input('What is your Name?').upper()}\n")
	print(f"\nYour name (in Title Case) is: {get_input('Both names please (in lower case)?').title()}")
	quit()


# Script runs from here: everything above is ignored until called
main() # call the function main()
