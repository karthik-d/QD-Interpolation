def y_intercept(pt1, pt2):
	x1, y1 = pt1 
	x2, y2 = pt2
	result = ((x2*y1)-(x1*y2))/(x2-x1)
	return result 

def slope(pt1, pt2):
	x1, x2 = pt1
	y1, y2 = pt2 
	result = (y2-y1)/(x2-x1)
	return result 