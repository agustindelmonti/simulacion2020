from collections import deque
import numpy as np
import os

folder = './results'
if not os.path.exists(folder):
    os.makedirs(folder)

def MM1(N,arrival_rate, service_rate):


	server_busy = False
	queue = deque([])
	tlast = 0
	events = [(np.random.exponential(arrival_rate),'A'),( float('inf'),'D')]

	total_waiting_time = 0
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

		#Statistical counters
		Qt += len(queue) * time_delta
		if server_busy:
			Bt += time_delta 

		#Arrival event
		if event[1] == 'A':
			arrival = np.random.exponential(arrival_rate) + clock
			if server_busy:
				queue.append(event[0])
			else: 
				num_delayed += 1
				server_busy = True
				departure = np.random.exponential(service_rate) + clock
				events[1] = (departure,'D')
			events[0] = (arrival,'A')

		#Departure event
		else:
			if len(queue) == 0:
				server_busy = False
				events[1] = (float('inf'),'D')
			else:
				wait = queue.popleft()
				total_waiting_time += clock - wait 
				num_delayed += 1
				departure = np.random.exponential(service_rate) + clock
				events[1] = (departure,'D')
		

	#Stats
	avg_system_time = total_waiting_time / clock
	avg_queue = Qt / N
	utilisation = Bt / clock 
	
	return avg_system_time,avg_queue, utilisation



def simulate(mu):
	n = 30
	lambda_ = 2
	avg_system_time = 0
	avg_queue = 0
	utilisation = 0
	for i in range(n):
		a,b,c = MM1(10000,lambda_,mu)

		avg_system_time += a
		avg_queue += b
		utilisation += c
        
	print(f'λ = {lambda_}  μ = {1/mu} ratio = {mu/lambda_} \nAvg. time in system: {avg_system_time/n}\nAvg. queue length: {avg_queue/n}\nBusy: {utilisation/n * 100}%\n')


if __name__ == "__main__":
	mus = [.5,1,1.5,2,2.5]
	for mu in mus:
		simulate(mu)