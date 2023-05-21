# does exactly the same as 07-Input1.py
# demonstrates use of string interpolation (f string)

def main():
	print("Hello. We are going to talk to each other...")
	print("I will ask you a question on screen.")
	print("You type a response and press Enter.")
	print()
	
	name = input("Type your name_")
	age = input("Type your age_")
	
	print(f"Hello {name}")				# note the f in front of opening quotes
	print(f"You are {age} years old")	# note the {} braces containing numbers, variables or even expressions eg {var * 5}

main()

input("Press Enter to quit")