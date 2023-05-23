import kboard as kb

def quit():
	input("Enter to quit")

# It is good coding practice to use a main() function
def main():
	#assume user is too lazy to use a capital letter
	'''
	kb.getString(prompt, withTitle, minInt, maxInt)
	prompt = "What is your name?", withTitle = False, min length 2, max length 20
	prompt = "Both names please?", withTitle = True, min length 4, max length 30
	'''
	
	print(f"\nYour name (in Caps) is: {kb.get_string('What is your Name?', False, 2, 20).upper()}\n")
	print(f"\nYour name (in Title Case) is: {kb.get_string('Both names please (in lower case)?', True, 4, 30)}")	
	quit()

# Script runs from here: everything above is ignored until called
main() # call the function main()