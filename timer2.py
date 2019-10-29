import time, ast, sys

def check():
	""" Returns entire dict of times"""
	f = open("timer.txt", "r")
	x = (f.read())
	x = ast.literal_eval(x)
	f.close()
	return x

def save(name,seconds):
	"""Writes Changes to timer file"""
	current = check()
	current[name] = seconds
	f = open("timer.txt", "w")
	f.write(str(current))
	f.close()

def pretty(n):
	""" Takes in time in seconds and converts to readable time"""
	hours = n // 3600
	mins = (n // 60) - 60 * hours
	secs = n % 60
	if n < 60:
		return str(secs) +" seconds"
	elif n < 3600:
		return str(mins) + " minutes, " + str(secs) + " seconds"
	else:
		return str(hours) + " hours, " +str(mins) + " minutes, " + str(secs) + " seconds"

def timer(name):
	""" Runs a timer and calls other functions to edit timer file"""
	timeElapsed = check()[name]

	print("Time on " + name + ": " +pretty(timeElapsed))
	print("Press Enter to Start Timer")
	dummy = input()
	
	t1 = time.time()
	print("Press Enter to Stop Timer")
	dummy = input()
	t2 = time.time()

	end = int(t2-t1)

	save(name, timeElapsed+end)

	print("")
	print("Time on " + name + ": " +pretty(timeElapsed+end))
	print("")
	menu()



def menu():
	""" Uses User input to call other functions"""
	print("1: Start a timer for a project")
	print("2: Start a new project")
	print("3: See all projects")
	print("4: Quit")
	choice = input()

	if choice == "1":
		print("Please enter project name")
		timer(input())

	elif choice == "2":
		print("Please enter project name")
		name = input()
		save(name,0)
		timer(name)
		

	elif choice == "3":
		for i in check():
			print(i,pretty(check()[i]))
		print("")

	elif choice == "4":
		sys.exit()

	else:
		print("Not a valid response. Please try again.")
	menu()

def main():
	menu()

main()

