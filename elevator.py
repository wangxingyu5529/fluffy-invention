"""
I live in a 10-floor building with 2 elevators. 
Ever since the quarantine, the elevator is limited with
one person or household per ride. But it wastes a lot of time
for a person to press the elevator button only to find out that
the elevator is already occupied (it also wastes the time of the
person who is already in the elevator). So what is an effective
algorithm/data structure for elevator?

Details to pay attention: 
- The two elevators will always return to default floors 1 and 5
respectively when no one requests a ride.
- If both elevators are free, the one closest to the new request
should take the order
"""


# Use queue to arrange incoming ride requests

class Request(object): 

	def __init__(arrival_time, from_floor, to_floor):
		self.arrival_time = arrival_time
		self.start_time = None
		self.from_floor = from_floor
		self.to_floor = to_floor

class Elevators(object): 

	def __init__(num_elevators):
		self.__line = queue.PriorityQueue(maxsize=num_elevators)

	def remove_person(self): 
		return self.__line.get(block=False)[1]

	def put_person(self, request):
		# the priorityqueue sort requests by arrival time
		return self.__line.put((request.arrival_time, request), block=False)

	def isfull(self): 
		return self.__line.full()
			



