from matplotlib import pyplot as plot

def get_xy_data(filename):
	x_data = list()
	y_data = list()
	with open(filename, 'r') as f:
		for line in f.readlines():
			elems = line.strip().split()
			if(len(elems)!=2):
				continue
			(x,y) = elems
			x_data.append(x)
			y_data.append(y)
	return x_data, y_data

def line_plot(axis, xy_data):
	axis.plot(xy_data[0], xy_data[1])

files = ['S1 WF', 'S1 WOF', 'S2 WF', 'S2 WOF', 'TL WF', 'TL WOF']
for idx, filename in enumerate(files):
	line_plot(plot.subplot(2, 3, idx+1), get_xy_data(filename))
plot.show()

# print(x_data[:50])
# print(y_data[:50])
