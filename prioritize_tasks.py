

if __name__ == "__main__":
	print("So many things to do! But you can get them done by prioritizing! One thing at a time.")
	print("This is the task list you had:")
	task_lst = []
	with open("tasks.txt", 'r') as f: 
		tasks = f.readlines()
		for task in tasks: 
			print(task)
			task_lst.append(task)
	print("Any tasks you would like to cross off?")
	ans = input()
	while ans != "No": 
		print("Which one did you finish? Seperate with comma")
		nums = list(map(int, input().split(',')))
		for n in sorted(nums, reverse=True): 
			task_lst.pop(n-1)
		print("Here are the tasks again")
		for task in task_lst: 
			print(task)
		print("Any other tasks you would like to cross off?")
		ans = input()

	print("Great")