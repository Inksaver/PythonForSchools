# demonstrates while loop and random
import random

def main():
	question = ""
	while question != "q": 
		# get an input from the user but do absolutely nothing with it except check for quit!
		question = input("Ask the magic 8 ball a question: (q to quit)_")
		answer = random.randint(0,8)  #returns a random whole number between 0 and 7
		if answer == 0:
			print("It is certain")
		elif answer == 1:
			print ("Outlook good")
		elif answer == 2:
			print ("You may rely on it")
		elif answer == 3:
			print ("Ask again later")
		elif answer == 4:
			print ("Concentrate and ask again")
		elif answer == 5:
			print ("Reply hazy, try again")
		elif answer == 6:
			print ("My reply is no")
		elif answer == 7:
			print ("My sources say no")
			
	input("Press Enter to quit")

main()

