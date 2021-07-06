import LinearParams
import csv

INTERVAL = 0.2

def linear_predict_y(pt1, pt2, req_x):
	result = (LinearParams.slope(pt1, pt2)*req_x) + LinearParams.y_intercept(pt1, pt2)
	return result

def generate_x(entries, start_x, start_y):
	precede = (start_x, start_y)
	follow = (start_x, start_y)
	curr_x = start_x 

	for row in entires:
		req_x = curr_x + INTERVAL
		pt = tuple(map(float, row[0].split()))
		pass

def run():
	fname = "S0 WOF"
	f_in = open(fname, 'r')
	
	entries = csv.reader(f_in, delimiter=' ')
	_ = next(entries)   # Skip header
	start_x, start_y = tuple(map(float, next(entries)[0].split()))

run()


