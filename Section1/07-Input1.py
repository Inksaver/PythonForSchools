# introducing variables
# string concatenation (nerd word meaning join) using .. <-2 dots

def main():
	print("Hello. We are going to talk to each other...") 	# Spooky!!!
	print("I will ask you a question on screen.")
	print("You type a response and press Enter.")
	print() 												# Print a blank line
	
	name = input("Type your name_")	# input() does NOT move to the next line
	age = input("Type your age_")	# input is a function: it returns a value which is stored in the variable age
	
	'''
	You can see we are using the input() built-in Python function
	var = input() # var is any variable such as name, age, height etc
	'''
	print("Hello " + name)
	print("You are " + age + " years old")			# the + joins words (strings) together

main()

input("Press Enter to quit") # function used as a procedure (The return value is discarded)