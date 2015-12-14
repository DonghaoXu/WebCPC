# Ray trace is to figure out how a ray is reflected/refracted at a surface
# It needs:
# 	1) a data structure to store ray trace data
#	2) to know surface material
#	3) to know the geometry of each surface
#	4) ending critria
from ray import ray

class raytrace:
	def __init__(self, geometry, numofrays=1000, maxpoints=10):
		self.__maxpoints = maxpoints
		self.numofrays = numofrays
		self.rays = []
		self.__geometry = geometry

	def initialize(self, coordinates, directions):
		'''
		Initialize the rays
		coordinates: An iterable data structure of (x, y, z)
		directions: An iterable data structure of (xvec, yvec, zvec)
		'''
		assert len(coordinates) == len(directions) == self.numofrays
		self.__directions = directions
		index = self.indef['init']
		for (x, y, z) in coor:
			r = ray()
			r.unlock()
			r.addPoint(x, y, z, index)
			r.lock()
			self.rays.append(r)


