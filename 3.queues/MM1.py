from collections import deque
import numpy as np



def MM1(N,arrival_rate=1, service_rate=1):

	server_busy = False
	queue = deque([])
	tlast = 0
	events = [(np.random.exponential(2),'A'),( float('inf'),'D')]

	total_delayed = 0
	num_delayed = 0
	Qt = 0
	Bt = 0
	clock = 0

	while num_delayed < N:
		#Simulation state
		event = min(events)
		tlast = clock
		clock = event[0]
		time_delta = (clock - tlast)

		#Arrival event
		if event[1] == 'A':
			arrival = np.random.exponential(arrival_rate) + clock
			events[0] = (arrival,'A')
			if server_busy:
				queue.append(arrival)
			else: 
				num_delayed += 1
				server_busy = True
				departure = np.random.exponential(service_rate) + clock
				events[1] = (departure,'D')

		#Departure event
		else:
			if len(queue) == 0:
				server_busy = False
				events[1] = (float('inf'),'D')
			else:
				wait = queue.popleft()
				total_delayed += clock - wait 
				num_delayed += 1
				departure = np.random.exponential(service_rate) + clock
				events[1] = (departure,'D')

		#Statistical counters
		Qt += len(queue) * time_delta
		if server_busy:
			Bt += time_delta 

	print(f'Avg. time delayed: {total_delayed / N}\nAvg. queue time: {Qt / N }\nBusy: {Bt / clock * 100}%')
	return 


if __name__ == "__main__":
	MM1(100000,10,7)

	