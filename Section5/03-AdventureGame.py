import kboard as kb
from dataclasses import dataclass
import time

'''
https://www.w3schools.com/charsets/ref_utf_box.asp
utf8 box characters stored here for easy copy/paste:

┌ ┬ ┐ ─ ╔ ╦ ╗ ═
 
├ ┼ ┤ │ ╠ ╬ ╣ ║
 
└ ┴ ┘   ╚ ╩ ╝
'''

@dataclass
class Item:	
	name = ""
	description = ""
	damage = 0
	value = 0

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
	
def create_items():
	''' 
	items uses a dictionary NOT a list 
	instead of items[0] use items["pencil"]
	to read / write to the item
	'''
	items = {} #empty dictionary
	
	key = "door key"
	items.update({key:Item()}) # add a new Item using the key "door key"-> also the name of the Item
	items[key].name = key
	items[key].description = "a Yale cylinder lock door key.\nMade of brass"
	items[key].damage = 5
	
	key = "pencil"
	items.update({key:Item()})
	items[key].name = key
	items[key].description = "a Derwent HB pencil.\nNeeds sharpening"
	items[key].damage = 20
	items[key].value = 5
	
	return items

def create_locations():
	''' 
	create locations. IMPORTANT ensure exits correspond:
	eg Classroom.toEast -> Corridoor therefore Corridoor.to_west = Classroom
	CHECK SPELLING! 'Corridoor' is NOT equal to 'corridoor'
	'''
	locations = []	#empty list
	
	locations.append(Location()) # add a new empty Location object to the list
	locations[0].name = "Classroom"	# set the name property
	locations[0].description = "The computer lab\nfurnished with steam driven PCs"	# set the description property
	locations[0].to_east = "Corridoor" # set the exit(s) as appropriate. They are empty sting by default
	locations[0].items = ["pencil"] # list of items in this location MAKE SURE Item with matching key is created ('pencil')
	
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
	locations[2].items = ["door key"]
		
	locations.append(Location())
	locations[3].name = "Outside"
	locations[3].description = "the playground: scattered empty plastic bottles\nnotice boards covered in grafitti"
	locations[3].to_north = "Corridoor"	
	
	return locations

def get_location_index(locations, location_name):
	for i in range(len(locations)):
		if locations[i].name == location_name:
			return i
	
	return -1 # will get here if error in finding location_name
	
def display_location(locations, current_location):
	exits = []	# empty list
	location_items = []
	location_index  = get_location_index(locations, current_location)
	if location_index > -1:	# must have found match as index  >= 0
		separator = "═" * 79 # repeat '═' 79 x
		location = locations[location_index] # eg "Classroom" (location.name)
		print(separator)
		print(f"You are in {location.name}, {location.description}")
		if location.to_north != "":
			exits.append(location.to_north)
		if location.to_east != "":
			exits.append(location.to_east)
		if location.to_south != "":
			exits.append(location.to_south)
		if location.to_west != "":
			exits.append(location.to_west)
		print("─" * 79 )
		location_items = location.items
		if len(location_items) > 0:
			output = ""
			for item in location_items:
				output += f"{item}, "
			print(f"Items here: {output}")
		else:
			print("There are no items in this area")
			
		print(separator)
		print()	
	else: # coding error ? mis-spelt location.name
		print(f"Unable to find location '{current_location}'")
			
	return exits, location_items

def display_player(player):
	separator = "═" * 79  # repeat '═' 79 x
	print(separator)
	print("\t\tPlayer Properties")
	print(f"    Name:     {player.name}")
	print(f"    Character:{player.character}")
	print(f"    Strength: {player.strength}")
	print(f"    Health:   {player.health}")
	print(f"    Mana:     {player.mana}")
	print(separator)
	print()		

def examine_item(items, menu_text):
	''' menu_text = "Examine ...'''
	item_name = menu_text[8:]
	print(f"The {item_name} is {items[item_name].description}\n")
	time.sleep(2)

def take_item(player, items, menu_text):
	''' menu_text = "Take ...'''
	item_name = menu_text[5:]
	player.inventory.append(item_name)
	print(f"You take the {item_name} and put it in your backpack\n")
	time.sleep(2)
	return item_name
	
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

def play(player, locations, current_location, items):
	''' game loop. Runs until user selects "Quit"  '''
	cmd = ""
	while cmd != "Quit":
		exits, location_items = display_location(locations, current_location) # returns available exits and items in current location
		location_index = get_location_index(locations, current_location) # gets the index of current_location
		if len(location_items) > 0: # at least 1 item found hanging
			exits.append("Interact with items") # add Interact to menu
		exits.append("Quit") # add "Quit" to menu
		choice = kb.menu("Choose your option", exits)
		cmd = exits[choice] # eg "Corridoor", "Interact with items", "Quit"
		if "Interact" in cmd: # "Interact with items"
			# run a second menu to examine/take/use/drop items
			while cmd != "Cancel Interaction": # cancel interaction
				options = []
				for item in location_items:
					options.append(f"Examine {item}")
					options.append(f"Take {item}")
				options.append("Cancel Interaction")
				choice = kb.menu("Choose your option", options)
				cmd = options[choice]
				if "Examine" in cmd: # user wants to examine something
					examine_item(items, cmd) # pass items dictionary, "Examine door key"
				elif "Take" in cmd: # user wants to take something
					item_key = take_item(player, items, cmd) # pass items dictionary, "Take door key"
					locations[location_index].items.remove(item_key) # remove item from location
					#location_items.remove(item_key) # remove item from recent list
					if len(locations[location_index].items) == 0: # no more items to examine / take
						cmd = "Cancel Interaction" # re-draw main menu
		else: # cmd is the name of a location
			current_location = cmd # could be "Quit" so loop will exit
					
def main():
	player = Player()				# create the player 
	player = update_player(player)	# ask user to input name/character
	display_player(player)			# display player properties
	items = create_items()			# create game items
	locations = create_locations()	# create locations
	current_location = "Classroom"	# set current location
	play(player, locations, current_location, items)
	
main()