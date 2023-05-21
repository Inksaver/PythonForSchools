'''
https://www.w3schools.com/charsets/ref_utf_box.asp
utf8 box characters stored here for easy copy/paste:

┌ ┬ ┐ ─ ╔ ╦ ╗ ═
 
├ ┼ ┤ │ ╠ ╬ ╣ ║
 
└ ┴ ┘   ╚ ╩ ╝
Use the template below to create an output that looks like one of these:
'''

'''
                                           Pre Windows 10 (1909) will not display UTF8
╔═══════════════════════════════════════╗  =========================================
║                                       ║  |                                       |
║	Welcome to Python programming!	    ║  |    Welcome to Python programming!     |
║		This line is tabbed in          ║  |        This line is tabbed in         |
║		So is this one!                 ║  |        So is this one!                |
╚═══════════════════════════════════════╝  +++++++++++++++++++++++++++++++++++++++++
'''
	
# Use print()
# use for example: print('=' * 8) to print '========'
# Can also use \t to line up the text
# The comment above is 5 lines of (42 characters)

def main():
	# method 1 use a complex string variable
	output = '''
╔═══════════════════════════════════════╗
║                                       ║
║    Welcome to Python programming!     ║
║        This line is tabbed in         ║
║        So is this one!                ║
╚═══════════════════════════════════════╝
	'''	
	print(output)
	
	# method 2 use either string multiplier or tab characters
	print(f"╔{'═' * 39}╗")
	print("║\t\t\t\t\t║")
	print("║    Welcome to Python Programming!\t║")
	print("║\tThis line is tabbed in  \t║")
	print("║\tSo is this one!\t\t\t║")
	print("╚═══════════════════════════════════════╝")
	
	print()
	
main()

input("Press Enter to quit")