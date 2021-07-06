import LinearParams
import csv

INTERVAL = 0.2

def predict_y(req_x, pt1, pt2):
	result = (LinearParams.slope(pt1, pt2)*req_x) + LinearParams.y_intercept(pt1, pt2)
	return result

def next_x(curr_x):
	return curr_x + INTERVAL

def record_row(pt, f_out):
	f_out.writerow(map(str, pt))

def generate_x(entries, curr_x, follow, precede):
	# Throws 'StopIteration' when no more entries left to read
	# follow & precede are wrt curr_x
	req_x = next_x(curr_x)
	while True:
		if(follow[0]>req_x):
			# Same preceding and following points
			return (False, (req_x, follow, precede))
		elif(follow[0]<req_x):
			# Push window ahead
			precede = follow
			follow = tuple(map(float, next(entries)[0].split()))
		else:
			# follow is the exact required point !
			return (True, follow)
		
def generate_rows(entries, f_out, start_x, start_y):
	follow = (start_x, start_y)
	precede = None
	req_x = start_x
	while True:
		try:
			exact, result = generate_x(entries, req_x, follow, precede)
		except StopIteration:
			break
		else:
			if(exact):
				record_row(result, f_out)
			else:
				req_x, follow, precede = result
				prediction = (round(req_x, 4), round(predict_y(req_x, precede, follow), 4))
				record_row(prediction, f_out)
		

def run(fname):
	f_in = open(fname, 'r')
	f_in_reader = csv.reader(f_in, delimiter=' ')
	_ = next(f_in_reader)   # Skip header
	start_x, start_y = tuple(map(float, next(f_in_reader)[0].split()))

	f_out = open(fname+'_gen', 'w')
	f_out_writer = csv.writer(f_out, delimiter=' ')
	generate_rows(f_in_reader, f_out_writer, start_x, start_y)

	f_in.close()
	f_out.close()

for fname in ['S0 WOF', 'S1 WF', 'S1 WOF', 'S2 WF', 'S2 WOF', 'TL WF', 'TL WOF', 'DS WOF']:
	run(fname)

x = predict_y(449.41399999998583, (449.03, -0.001), (449.442, -0.001))
print(round(x,4))
print(predict_y(0, (-4,0), (2,12)))


