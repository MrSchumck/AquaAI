#Import required libraries
import sys
import os
#filecheck=os.path.isfile("AI.pl")
#Check if the file exists
filecheck=os.path.isfile("AI.dat")
#If the file exists, ask for a username
if filecheck == 1:
	with open('AI.dat', 'r') as file:
		contents=file.read()
	username=raw_input("What is your username?: ")
	#If the user is in AI.dat and has their own file
	if username.lower() in contents and os.path.isfile("%s.pl" %username):
		#Open the commands file
		file=open('Commands.dat', 'a')
		#Begin a loop
		while True:
			print("Welcome %s, how may I help you?" %username)
			#Ask for a command
			command=raw_input("Enter Command: ")
			#If a period is in the command, save it to a file
			if "." in command.lower():
				file.write(command.lower())
				file.write("\n")
			elif "?" in command:
				readfile=open('Commands.dat', 'r')
				query=command.lower()
				query=query.split("is ", 1)[1]
				query=query.split("?", 1)[0]
				#Search for answer in Commands.dat
				for line in readfile:
					line=line.rstrip()
					if query in line:
						answer=line
						exit
				query=query.split("my", 1)[1]
				answer=answer.split("is", 1) [1]
				print("Your %s is: %s" %(query, answer))
				
		
else:
	print("Welcome to the AquaAI setup.")
	print("No spaces or special characters allowed.")
	#Ask for the username
	username=raw_input("What is your name(all lowercase)?: ")
	#Save the username in lowercase
	username=username.lower()
	print("Hello, %s, please answer a few questions about yourself:" %username)
	#Get the user's favorite color
	color=raw_input("What is your favorite color?: ")
	#Get the user's birthday
	birthday=raw_input("When is your birthday (month/day in numbers)?: ")
	#Write the username to a file
	with open('AI.dat', 'w') as file:
		file.write("%s" %username)
		file.write("\n")
	#Write user information to a prolog file
	with open('%s.pl' %username, 'w') as file:
		file.write("favoritecolor(%s)." %color)
		file.write("\n")
		file.write("birthday(%s)." %birthday)
	with open('Commands.dat', 'w') as file:
		file.write("")
