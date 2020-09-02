from time import sleep


if __name__ == "__main__":
	print("So many things to do! But you can get them done by prioritizing! One thing at a time.\n"); sleep(0.5)
	print("This is the task list you had: \n"); sleep(1)
	task_lst = []

	# Read task list
	with open("tasks.txt", 'r') as f: 
		tasks = f.readlines()
		for task in tasks: 
			print(task[:-1]); sleep(0.5)
			task_lst.append(task[:-1])
	print("Any tasks you would like to cross off? Yes or No")
	ans = input()

	# Delete finished tasks
	while ans != "No": 
		print("Which one did you finish? Separate with comma")
		to_remove = input().split(', ')
		for x in sorted(to_remove, reverse=True): 
			if x not in task_lst: 
				print("There seems to be a typo. Try it again?")
			else: 
				task_lst.remove(x)
		print("I have crossed them off. Here are the tasks again:\n"); sleep(1)
		for task in task_lst: 
			print(task); sleep(0.5)
		print("Any other tasks you would like to cross off? Yes or No")
		ans = input()
	print("\nNo problem. \n")

	# Add new tasks to the appropriate place
	print("Any task you would like to add?")
	ans = input()
	while ans != "No":
		print("\nWhat is the name of the task?")
		name = input()
		task_lst.append(name)
		n = len(task_lst)

		for i in range(n-2, -1, -1):
			print("Is {} more important than {}".format(name, task_lst[i]))
			if input() == "Yes":
				task_lst[i+1], task_lst[i] = task_lst[i], task_lst[i+1]
			else: 
				break
		print("We have added {} to the list. Here is your new to-do-list.".format(name))

		for x in task_lst: 
			print(x); sleep(0.5)

		print("Do you want to add another task? Yes or No")
		ans = input()

	with open('tasks.txt', 'w') as f: 
		f.writelines([task+"\n" for task in task_lst])

	print("Great. I have updated your to-do-list.")
