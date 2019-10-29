import time, glob, os


def timer(name):
	f = open(name+".txt", "r")
	timeElapsed = (f.read())
	if timeElapsed == "":
		timeElapsed = 0
	else:
		timeElapsed = int(timeElapsed)
	f.close()
	print(timeElapsed)
	t1 = time.time()
	print("Press Enter to Stop Timer")
	dummy = input()
	t2 = time.time()



	end = int(t2-t1)

	f = open(name+".txt", "w")
	f.write(str(timeElapsed+end))
	f.close()




def menu():
	print("1: Start a timer for the current session")
	print("2: See how much time you spent on a given project")
	print("3: See how time you have spent on all projects")
	print("4: Quit")
	choice = input()
	#choice = "1"
	if choice == "1":
		print("Please enter project name")
		timer(input())
		#timer("test")
	elif choice == "4":
		print("bye!")
		return False
	else:
		print("Not a valid response. Please try again.")
	return True

def main():
	menu()

main()

