



class surf:
	def __init__(self, func, scope, material, flag):
		'''
		Input:
			func: the function that describe the surface
			scope: the range of x coordinate that func governs.
				dictionary with keys as ['x', 'y', 'z'] and values of tuples [low, high]
			material: material instance
			flag: true if refraction is considered; false if reflection is considered
		'''
		self.func = func
		self.scope = scope
		self.refract = flag
		self.__mat = material
		

	# def 