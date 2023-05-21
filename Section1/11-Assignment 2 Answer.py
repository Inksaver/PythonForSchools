'''
https://www.w3schools.com/charsets/ref_utf_box.asp
utf8 box characters stored here for easy copy/paste:

┌ ┬ ┐ ─ ╔ ╦ ╗ ═
 
├ ┼ ┤ │ ╠ ╬ ╣ ║
 
└ ┴ ┘   ╚ ╩ ╝

Use the template below to create an output that looks like one of these: (either UTF8 or ASCII)

╔════════════════════════════════════╗    --------------------------------------
║    Personal Data Collection App    ║    |    Personal Data Collection App    |
╚════════════════════════════════════╝    --------------------------------------
Please type your first name_              Please type your first name_
How old are you?_                         How old are you?_
What month is your birthday?_             What month is your birthday?_

══════════════════════════════════════    --------------------------------------

Thank you for sharing your data.          Thank you for sharing your data.
It will now be sold to scam websites.     It will now be sold to scam websites. 
This is what we know about you:           This is what we know about you:

╔════════════════════════════════════╗    +++++++++++++++++++++++++++++++++++++++
║	Name:                            ║    +    Name:                            +
║	Age:                             ║    +    Age:                             +
║	Birth Month:                     ║    +    Birth Month:                     +
╚════════════════════════════════════╝    +++++++++++++++++++++++++++++++++++++++

'''

# create 3 variables called name, age, month to store the data
# use print(), input()
# create a decorative output similar to the examples

def main():
	separator = "═" * 40			# repeat '═' 40 x
	box_top = f"╔{separator}╗"		# add additional chacacters to start / end
	box_bottom = f"╚{separator}╝"	# add additional chacacters to start / end
	
	print(box_top)
	print("║    Personal Data Collection App        ║")
	print(box_bottom)
	print()
	
	name = input("Please type your first name_")
	age = input("How old are you?_")
	month = input("What month is your birthday?_")
	
	print()
	print(separator)
	
	print("Thank you for sharing your data.\n" +
		  "It will now be sold to scam websites.\n" +
		  "This is what we know about you:\n")
	print(box_top)
	print(f"║  Name:        {name}{' ' * (25 - len(name))}║")
	print(f"║  Age:         {age}{' ' * (25 - len(str(age)))}║")
	print(f"║  Birth Month: {month}{' ' * (25 - len(month))}║")
	print(box_bottom)

main()								# program starts here

input("Press Enter to quit>")