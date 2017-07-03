# Author: Beshoy Megalaa

import sys

# init alloccation matrix based on user input (# of processes)
# Process and stores input as integers into alloccation matrix
def init_alloccation_matrix(process):
	alloccation_matrix = []

	# init alloccation matrix
	alloccation_matrix = [[0 for i in range(4)] for j in range(process)]

	i = 0	# Row index in the matrix
	j = 0	# Col index in the matrix row
	proc_num = 1 # for output formatting only
	while(process != 0):

		# input() reads strings, however it recognizes integer's input as int object which not iterable
		# Explicitetly convert user's inpurt to a string to iterate over
		alloccation_vector = str(input("Enter alloccation vector for process {} (ex. 1234): ".format(proc_num)))

		# Iterate over each item in string, convert to an int, then assign it in its appropriate location in allocc matrix
		# Increment j for the next colume
		for x in alloccation_vector:
			alloccation_matrix[i][j] = int(x)
			j += 1 

		# Rest the col, but keep the current row
		i += 1
		j = 0

		# Increment for next process
		process -= 1
		proc_num += 1

	print_matrix(alloccation_matrix)
	return alloccation_matrix

# init claim matrix based on user input (# of processes)
# Process and stores input as integers into claim matrix
def init_claim_matrix(process):
	claim_matrix = []

	# init claim matrix
	claim_matrix = [[0 for i in range(4)] for j in range(process)]

	i = 0	# Row index in the matrix
	j = 0	# Col index in the matrix row
	proc_num = 1 # for output formatting only
	while(process != 0):

		# input() reads strings, however it recognizes integer's input as int object which not iterable
		# Explicitetly convert user's inpurt to a string to iterate over
		claim_vector = str(input("Enter claim vector for process {} (ex. 1234): ".format(proc_num)))

		# Iterate over each item in string, convert to an int, then assign it in its appropriate location in claim matrix
		# Increment j for the next colume
		for x in claim_vector:
			claim_matrix[i][j] = int(x)
			j += 1 

		# Rest the col, but keep the current row
		i += 1
		j = 0

		# Increment for next process
		process -= 1
		proc_num += 1

	print_matrix(claim_matrix)
	return claim_matrix

# init resource vector based on user input
def init_resource_vector():
	resource_vector = [0,0,0,0]

	get_resource_vector = str(input("Enter resource vector (ex. 1234): "))

	# Process user's resource vector
	i = 0 
	for x in get_resource_vector:
		resource_vector[i] = int(x)
		i += 1
	print(resource_vector)
	return resource_vector

# Available vector = resource vector - sum of alloccation matrix
def compute_avail_vector(alloc, reso):
	avail_vector = []
	r1 = r2 = r3 = r4 = 0	# Row1, Row2, Row3, Row4 in alloccation matrix
	
	# Compute the sum of each row in alloccation matrix
	for row in alloc:
		i = 0 
		r1 += row[i]
		i += 1
		r2 += row[i]
		i += 1
		r3 += row[i]
		i += 1
		r4 += row[i]

	# Store sums temporary in available vector
	avail_vector = [r1,r2,r3,r4]

	# Check if there are enough resources
	# Compute each alloc col sum and compare it with resource vector
	i = 0
	for value in reso:
		if(value < avail_vector[i]):
			print("You alloccated more than available resources, terminating . . .")
			sys.exit()
		i += 1

	# Subtract resource vector from sum of allocc matrix rows (avail_vector)
	i = 0
	for value in reso:
		avail_vector[i] = value - avail_vector[i]
		i += 1
		
	print("The available vector: {}".format(avail_vector))
	return avail_vector

# request matrix = Claim matrix - alloccation matrix
def compute_request_matrix(alloc, claim, process):
	request_matrix = [[0 for i in range(4)] for j in range(process)]

	# Computes the request matrix
	i = j = 0 # i is the row number, j is col number (fixed to 4)
	while(i < process):
		while(j < 4):
			request_matrix[i][j] = claim[i][j] - alloc[i][j]
			j += 1
		i += 1
		j = 0

	print("The C-A matrix: ")
	print_matrix(request_matrix)
	return request_matrix

# Checks for deadlock
def check_deadlock(alloc, avail, request, process):

	# Checks for deadlock, break once a process can proceed is found
	good_row = []	# Row to be returned
	good_row_index = 0	# Index of returned row
	deadlock = False 	# Initial deadlock state is false

	for request_row in request:
		j = 0	# Row indexer
		i = 0	# Col indexer
		sum = 0
		for value in request_row:
			if value > avail[i]:	# value = avail[i] IS GOOD i.e no deadlock
				deadlock = True
				break 	# Break of current row
			else:
				deadlock = False
				#sum += value		
			i += 1


		# Break if there at ONE row to proceed
		# not deadlock = a good row
		if(not deadlock):
			#print("J index {}".format(j))
			good_row = request[j]
			good_row_index = j
			del request[j] # Reset request row
			#print(good_row_index)
			break
		j += 1	# Update row #BUG IF FIRST ROW IS GOOD FIX IT

	if(deadlock):
		print("Unsafe state: deadlock will occur, terminating . . .")
		sys.exit()
	else:
		print("Safe state: deadlock will not occur. ")

	# Returns FALSE
	return deadlock, good_row, good_row_index

# Checks for safe/unsafe state
def check_state(alloc, claim, avail, request, process):

	deadlock = check_deadlock(alloc, avail, request, process)

	# Stimulate the algorithm, safe/unsafe 
	while(not deadlock[0] and (process != 0)):

		i = 0
		for value in avail:
			avail[i] =  alloc[deadlock[2]][i] + value
			alloc[deadlock[2]][i] = 0
			i += 1

		process -= 1
		deadlock = check_deadlock(alloc, avail, request, process)

	#print(avail)
	#print_matrix(alloc)
	#print_matrix(request)

# Utility function to print matrix
def print_matrix(matrix):
	for row in matrix:
		print(row)

def main():

	correct_input =  False
	while(not correct_input):
		try:
			num_processes = int(input("How many processes (ex. 1, 5)? "))
			correct_input = True
		except:
			print("Invalid Input")


	a = init_alloccation_matrix(num_processes)
	c = init_claim_matrix(num_processes)
	r = init_resource_vector()
	v = compute_avail_vector(a,r)
	n = compute_request_matrix(a,c, num_processes)
	check_state(a,c,v,n, num_processes)

if __name__ == "__main__":
	main()