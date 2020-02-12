import numpy as np

def test_distance(point1, point2):

	point1 = np.array(point1)
	point2 = np.array(point2)
	return np.linalg.norm(point1-point2)

