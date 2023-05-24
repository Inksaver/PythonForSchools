import kboard as kb
from dataclasses import dataclass

'''
https://www.w3schools.com/charsets/ref_utf_box.asp
utf8 box characters stored here for easy copy/paste:

┌ ┬ ┐ ─ ╔ ╦ ╗ ═
 
├ ┼ ┤ │ ╠ ╬ ╣ ║
 
└ ┴ ┘   ╚ ╩ ╝
'''

@dataclass
class Player:
	name = ""
	character = ""
	strength = 0
	health = 0 
	mana = 0
	hitpoints = 100
	inventory = []
	characters = ["Swot", "Nerd", "Dunce", "Bully"]
	
@dataclass
class Location:
	name = ""
	description = ""
	to_north = ""
	to_east = ""
	to_south = ""
	to_west = ""
	items = []

def create_locations():
	''' 
	create locations. IMPORTANT ensure exits correspond:
	eg Classroom.toEast -> Corridoor therefore Corridoor.to_west = Classroom
	'''
	locations = []	#empty list
	
	locations.append(Location()) # add a new empty Location object to the list
	locations[0].name = "Classroom"	# set tne name property
	locations[0].description = "The computer lab\nfurnished with steam driven PCs"	# set the description property
	locations[0].to_east = "Corridoor" # set the exit(s) as appropriate
	
	locations.append(Location())
	locations[1].name = "Corridoor"
	locations[1].description = "narrow passage filled with pupils,\nscattered trainers and bags.\nIs that weed I can smell?"
	locations[1].to_north = "Office"
	locations[1].to_south ="Outside"
	locations[1].to_west = "Classroom"
	
	locations.append(Location())
	locations[2].name = "Office"
	locations[2].description = "Head teachers office. \nA well used cane hanging from a hook. \nHalf empty whisky bottle on the desk"
	locations[2].to_south = "Corridoor"

	locations.append(Location())
	locations[3].name = "Outside"
	locations[3].description = "the playground: scattered empty plastic bottles\nnotice boards covered in grafitti"
	locations[3].to_north = "Corridoor"	
	
	return locations
	
def display_location(locations, current_location):
	directions = []	# empty list
	location_index  = -1 # initialised to -1
	for i in range(len(locations)):
		if locations[i].name == current_location:
			location_index = i
			break
	if location_index > -1:	# must have found match as index  >= 0
		separator = "═" * 79			# repeat '═' 79 x
		location = locations[location_index]
		print(separator)
		print(f"You are in {location.name}, {location.description}")
		if location.to_north != "":
			directions.append(location.to_north)
		if location.to_east != "":
			directions.append(location.to_east)
		if location.to_south != "":
			directions.append(location.to_south)
		if location.to_west != "":
			directions.append(location.to_west)
		print(separator)
		print()	
	else: # coding error ? mis-spelt location.name
		print(f"Unable to find location '{current_location}'")
			
	return directions

def display_player(player):
	separator = "═" * 79			# repeat '═' 79 x
	print(separator)
	print("\t\tPlayer Properties")
	print(f"    Name:     {player.name}")
	print(f"    Character:{player.character}")
	print(f"    Strength: {player.strength}")
	print(f"    Health:   {player.health}")
	print(f"    Mana:     {player.mana}")
	print(separator)
	print()		
	
def update_player(player):
	player.name = kb.get_string("Type a name for your player (3-15 characters)", True, 3, 15)
	choice = kb.menu("Choose a character", player.characters) # choice is an integer between 0 and the length of list-1
	player.character = player.characters[choice] # get the name from the list of characters
	if choice == 0: # Swot
		player.strength = 80
		player.health = 90
		player.mana = 70
	elif choice == 1: # Nerd
		player.strength = 70
		player.health = 100
		player.mana = 60
	else: # Dunce, Bully or any others
		player.strength = 50
		player.health = 50
		player.mana = 0		
	# complete this if block to change values for all characters
	
	return player

def play(player, locations, current_location):
	''' game loop. Runs until user selects "Quit"  '''
	while current_location != "Quit":
		directions = display_location(locations, current_location)
		directions.append("Quit")
		choice = kb.menu("Which direction?", directions)
		current_location = directions[choice]

def main():
	player = Player()				# create the player 
	player = update_player(player)	# ask user to input name/character
	display_player(player)			# display player properties
	locations = create_locations()	# create locations
	current_location = "Classroom"	# set current location
	play(player, locations, current_location)
	
	input("Enter to quit") 
	
main()