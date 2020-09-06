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

queue_request = []

elevator1 = Elevator(1)
elevator2 = Elevator(5)

while True: 
	if len(queue_request) == 0: 
		elevator.current_floor = self.default_floor
	else: 
		if (not elevator1.occupied) and (not elevator2.occupied):
			


class Elevator: 
	def __init__(default_floor):
		self.default_floor = default_floor
		self.current_floor = default_floor # We denote basement as floor 0
		self.occupied = False

	def incoming_request(from_floor):
