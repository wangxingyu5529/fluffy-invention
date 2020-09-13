'''
Recently I've been playing Werewolf/Mafia with friends over Zoom. 
This is a program that can automatically assign roles to people.
'''
from random import shuffle

role_dict = {
	7: ['mafia'] * 2 + ['cop', 'doctor'] + ['townies'] * 3,
	8: ['werewolf'] * 3 + ['prophet', 'witch', 'hunter'] + ['townies'] * 2,
	9: ['werewolf'] * 3 + ['prophet', 'witch', 'hunter'] + ['townies'] * 3,
	10: ['werewolf'] * 3 + ['prophet', 'witch', 'hunter'] + ['townies'] * 4,
	11: ['werewolf'] * 4 + ['prophet', 'witch', 'hunter', 'idiot'] + ['townies'] * 3,
}

def generate_roles(names):
	'''
	Input: 
		names (list): list of player's names

	Output: 
		list of tuples of the form (name, role)
	'''
	n = len(names)
	shuffle(names)
	return list(zip(names, role_dict[n]))
