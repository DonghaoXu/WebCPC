#! encoding: utf-8
import numpy as np

class ray:
	'''
	Class to store ray trace data including x, y coordinates and indices
	'''
	def __init__(self):
		# self.__maxpoints = maxpoints
		self.__x = []
		self.__y = []
		self.__z = []
		self.__index = []
		self.__cur = 0 # the current position waiting to be filled
		self.__editable = False

	def __str__(self):
		'''
		Print the trace of the ray
		'''
		print self.getAll()
		head = 'x\ty\tz\ttheta_i\tindex\n'
		body = [str(round(x, 2)) + '\t' 
			+ str(round(y, 2)) + '\t' 
			+ str(round(z, 2)) + '\t'
			+ str(round(np.rad2deg(ia), 2)) + '\t'
			+ str(index) + '\n'
			for (x, y, z, ia, index) in self.getAll()]
		return head + ''.join(body)

	def getAll(self):
		'''
		Tuple of (x, y, z, index)
		'''
		return zip(self.__x, self.__y, self.__z, self.getIncidentAngle(), self.__index)

	def getX(self):
		'''
		Return x coordinates
		'''
		return self.__x

	def getY(self):
		'''
		Return y coordinates
		'''
		return self.__y

	def getZ(self):
		'''
		Return z coordinates
		'''
		return self.__z

	def getCoordinates(self):
		'''
		Tuple of (x, y, z) coordinates
		'''
		return zip(self.__x, self.__y, self.__z)

	def getIncidentAngle(self):
		'''
		List of incident angles
		'''
		vec = np.diff(np.array(self.getCoordinates()))
		vec1 = vec[:-2, :]
		vec2 = vec[1::, :]
		ia = [0]
		ia.extend([(np.pi - np.arccos(np.dot(v1, v2) / 
			np.linalg.norm(v1) / np.linalg.norm(v2))) / 2 
			for (v1, v2) in zip(vec1, vec2)])
		ia.append(0)
		return ia

	def getIndices(self):
		'''
		The indices of incident surfaces
		'''
		return self.__index

	def getCur(self):
		'''
		Return the current position to be filled by data
		'''
		return self.__cur

	def getNumofPoints(self):
		'''
		Return the total number of incident points in the instance
		'''
		return self.__cur

	def lock(self):
		'''
		Lock the instance
		'''
		self.__editable = False

	def unlock(self):
		'''
		Unlock the instance
		'''
		self.__editable = True

	def iseditable(self):
		'''
		Return true if the instance is editable; otherwise false
		'''
		return self.__editable

	def addPoint(self, x, y, z, index):
		'''
		Add an incident point to the instance
		'''
		if self.__editable:
			self.__x.append(x)
			self.__y.append(y)
			self.__z.append(z)
			self.__index.append(index)
			self.__cur += 1
		else:
			print 'Instance is locked.'

	def dropPoint(self):
		'''
		Drop last incident point
		'''
		if self.__editable and self.__cur > 0:
			self.__x.pop()
			self.__y.pop()
			self.__z.pop()
			self.__index.pop()
			self.cur -= 1

	def toy(self, n=10):
		'''
		Make a toy instance with random data
		'''
		newray = ray()
		newray.unlock()
		rnd = np.random.rand
		rndi = np.random.randint
		for (x, y, z, i) in zip(rnd(n), rnd(n), rnd(n), rndi(n, size=n)):
			newray.addPoint(x, y, z, i)
		newray.lock()
		return newray


if __name__ == '__main__':
	a = ray()
	a = a.toy()
	# print a.getAll()
	# print a.getIncidentAngle()
	print a

	

