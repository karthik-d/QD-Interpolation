import LinearParams
import csv

INTERVAL = 0.2

def linear_predict_y(pt1, pt2, req_x):
	result = (LinearParams.slope(pt1, pt2)*req_x) + LinearParams.y_intercept(pt1, pt2)
	return result

def next_x(curr_x):
	return curr_x + INTERVAL

def generate_x(entries, curr_x, follow, precede):
	req_x = next_x(curr_x)
	while True:
		try:
			if(follow[0]>req_x):
				# Same preceding and following points
				return (False, req_x, follow, precede)
			elif(follow[0]<req_x):
				# Push window ahead
				precede = follow
				follow = tuple(map(float, next(entries)[0].split()))
			else:
				# Follow is the exact required point !
				return (True, follow)
		except StopIteration:
			break
		
def generate_rows(entries, start_x, start_y):
	precede = (start_x, start_y)
	exact, result = generate_x(entries, start_x, precede)
	for exact, result in generate_x(entries, start_x, precede):
		if(exact):
			print(result)
		else:
			req_x, follow, precede = result 
			print(req_x, follow, precede)

def run():
	fname = "S0 WOF"
	f_in = open(fname, 'r')
	
	entries = csv.reader(f_in, delimiter=' ')
	_ = next(entries)   # Skip header
	start_x, start_y = tuple(map(float, next(entries)[0].split()))
	generate_rows(entries, start_x, start_y)

run()


