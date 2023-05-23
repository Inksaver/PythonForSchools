import kboard as kb # shortens the class name to kb

def main():
	user_name = kb.get_string("Type your name", True, 3, 6) 			# returns user input in Title Case
	user_age = kb.get_integer("How old are you", 5, 120) 				# gets an integer between 5 and 120 from the user
	user_height = kb.get_float("How tall are you in metres?", 0.5, 2.5) # gets a float between 0.5 and 2.5 from the user
	user_likes_python = kb.get_boolean("Do you like Python? (y/n)") 	# returns True or False from the user
	
	print(f"User name : {user_name}")
	print(f"User age : {user_age}")
	print(f"User height : {user_height}")
	print(f"User likes Python : {user_likes_python}")
	print()
	menu_list = ["Brilliant", "Not bad", "Could do better", "Rubbish"]
	user_choice = kb.menu("What do think of this utility?", menu_list)
	print(f"User thinks this utility is: {menu_list[user_choice]}")
	
	# if running from a console/terminal instead of an IDE to prevent closing.
	kb.get_string("Press Enter to Quit", False, 0, 20) # Used instead of input("Press Enter to Quit")
	
main()