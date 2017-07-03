# Author: Beshoy Megalaa

import sys

# init alloccation matrix based on user input (# of processes)
# Process and stores input as integers into alloccation matrix
def init_alloccation_matrix(process):
	alloccation_matrix = []

	# init alloccation matrix
	alloccation_matrix = [[0 for i in range(5)] for j in range(process)]

	i = 0	# Row index in the matrix
	j = 0	# Col index in the matrix row
	proc_num = 1 # for output formatting only
	while(process != 0):

		# input() reads strings, however it recognizes integer's input as int object which not iterable
		# Explicitetly convert user's inpurt to a string to iterate over
		alloccation_vector = str(input("Enter alloccation vector(A) for process {} (ex. 12345): ".format(proc_num)))

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

# init request matrix based on user input (# of processes)
# Process and stores input as integers into request matrix
def init_request_matrix(process):
	request_matrix = []

	# init request matrix
	request_matrix = [[0 for i in range(5)] for j in range(process)]

	i = 0	# Row index in the matrix
	j = 0	# Col index in the matrix row
	proc_num = 1 # for output formatting only
	while(process != 0):

		# input() reads strings, however it recognizes integer's input as int object which not iterable
		# Explicitetly convert user's inpurt to a string to iterate over
		request_vector = str(input("Enter request vector(Q) for process {} (ex. 12345): ".format(proc_num)))

		# Iterate over each item in string, convert to an int, then assign it in its appropriate location in request matrix
		# Increment j for the next colume
		for x in request_vector:
			request_matrix[i][j] = int(x)
			j += 1 

		# Rest the col, but keep the current row
		i += 1
		j = 0

		# Increment for next process
		process -= 1
		proc_num += 1

	print_matrix(request_matrix)
	return request_matrix

# init resource vector based on user input
def init_resource_vector():
	resource_vector = [0,0,0,0,0]

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
	r1 = r2 = r3 = r4 = r5 = 0	# Row1, Row2, Row3, Row4 in alloccation matrix
	
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
		i += 1
		r5 += row[i]

	# Store sums temporary in available vector
	avail_vector = [r1,r2,r3,r4,r5]

	# Check if there are enough resources
	# Compute each alloc col sum and compare it with resource vector
	i = 0
	for value in reso:
		if(value < avail_vector[i]):
			print("You allocated more than available resources, terminating . . .")
			sys.exit()
		i += 1

	# Subtract resource vector from sum of allocc matrix rows (avail_vector)
	i = 0
	for value in reso:
		avail_vector[i] = value - avail_vector[i]
		i += 1
		
	print("The available vector(W): {}".format(avail_vector))
	return avail_vector

def detection(process, alloc, req, avail):
	# 1) Check if there is a row in request matrix Q that is less 
	#	 than avail vector W, mark row and break once found,
	#	 otherwise if no row found end program.
	#	 Delete the returned Q row since it has been satisfied

	print("\nApplying the deadlock detection algorithm")

	while(len(req) != 0):

		j = 0	# Row index
		for q_row in req:
			i = 0	# Col index
			good_row_flag = False
			for value in q_row:
				if(value > avail[i]):
					good_row_flag = False
					j += 1 #Update row first
					row_marked = j
					break;	# Break out of current row, move to next row
				else:
					good_row_flag = True
				i += 1
				row_marked = j
			if(good_row_flag):
				break

		if(good_row_flag == False):
			print("Deadlock: no row in Q is less than or equal to W, terminating . . .")
			sys.exit()

		del req[j]	# To avoid the row being considered again IMPORTANT

		# 2) Locate the same row location in allocation matrix A.
		# 3) W = W + A(Process)

		i = 0
		for value in avail:
			avail[i] = avail[i] + alloc[row_marked][i]
			i += 1
		print("Updated W {}, P{} marked".format(avail, row_marked))

		# 4) Goto step 1
	print("Deadlock detection algorithm ended")

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
			if(num_processes == 0):
				correct_input = False
		except:
			print("Invalid Input")

	a = init_alloccation_matrix(num_processes)
	req = init_request_matrix(num_processes)
	res = init_resource_vector()
	v = compute_avail_vector(a,res)

	detection(num_processes, a, req, v)
if __name__ == "__main__":
	main()