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
	characters = ["Wizard", "Priest", "Fighter", "Ninja"]

def display_player(player):
	separator = "═" * 40			# repeat '═' 40 x
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
	choice = kb.menu("Choose a character", player.characters)
	player.character = player.characters[choice]
	if choice == 0: # Wizard
		player.strength = 80
		player.health = 90
		player.mana = 70
	elif choice == 1: # Priest
		player.strength = 70
		player.health = 100
		player.mana = 60
	else:
		player.strength = 50
		player.health = 50
		player.mana = 0		
	# complete this if block to change values for all characters
	
	return player

def main():
	player = Player()
	player = update_player(player)
	display_player(player)
	
	input("Enter to quit")
	
main()