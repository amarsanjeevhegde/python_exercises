# if statement to generate random number
import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))



   

# while/if statement to get the answer
dice = "yes"

while dice == "yes":
	
	# Gnenerates a random number between 1 and 6 
	no = random.randint(1,6)
	
	if no == 1:
		print("[1]")

	if no == 2:
		print("[2]")

	if no == 3:
		print("[3]")

	if no == 4:
		print("[4]")

	if no == 5:
		print("[5]")

	if no == 6:
		print("[6]")

		
	dice =input("press yes to roll again and no to exit:")
	print("\n")
