"""
I live in a 10-floor building with 2 elevators. 
Ever since the quarantine, the elevator is limited with
one person or household per ride. But it wastes a lot of time
for a person to press the elevator button only to find out that
the elevator is already occupied (it also wastes the time of the
person who is already in the elevator). So what is an effective
algorithm/data structure for elevator?

The program needs to accomplish the following: 
- The two elevators will always return to default floors 1 and 5
respectively when no one requests a ride.
- If both elevators are free, the one closest to the new request
should take the order. If an elevator is occupied, it should not
take any other order, so no two households will share the same
ride. 
- Simulate an elevator situation, with random floor request being
generated and processed
"""


# Use queue to arrange incoming ride requests

import random

class Request(object): 

	def __init__(self, arrival_time, from_floor, to_floor):
		self.arrival_time = arrival_time # use integers to represent time here
		self.from_floor = from_floor
		self.to_floor = to_floor

	def __lt__(self, other):
		# comparison for generating heap later on
		return self.arrival_time < other.arrival_time

	def __repr__(self):
		return "Request: arrival_time = {}, from_floor = {}, to_floor = {}".format(
			self.arrival_time, self.from_floor, self.to_floor)

class Elevator(object): 

	def __init__(default_floor):
		self.default_floor = default_floor
		self.occupied = False


def generate_random_requests(num_requests):
	'''
	Input: 
		num_requests: the number of requests that will be generated
		in this simulation
	Output: (list) a list of requests objects
	'''

	requests_floors = random.sample(range(-1, 11), num_requests)
	# we take the index of requests_floors to be the arrival time
	requests_lst = []
	for arrival_time, from_floor in enumerate(requests_floors): 
		if from_floor == 1: 
			# if a person enters from floor one, they will only
			# go to other floors
			to_floor = random.choice([-1] + list(range(2, 11)))
		elif from_floor == -1: 
			to_floor = random.choice(range(1, 11))
		else: 
			# if a person did not come from floor 1 or basement, 
			# this person wants to go to floor 1 or basement
			to_floor = random.choice([-1, 1])
		print(arrival_time, from_floor, to_floor)
		request = Request(arrival_time, from_floor, to_floor)
		requests_lst.append(request)
	return requests_lst


def simulate(num_requests):
	'''
	Input: 
		num_requests: the number of requests that will be generated
		in this simulation
	'''
	requests_lst = generate_random_requests(num_requests)
	



