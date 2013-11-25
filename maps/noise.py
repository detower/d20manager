import random

class Perlin(object):
	def __init__(self, w,h, rmin=-16, rmax = 16, smoothings = 1):
		self.matrix = []
		self.w = w
		self.h = h
		self.mountain_coord = None
		self.marianne_coord = None
		self.mountain = rmin
		self.marianne = rmax

		self.smoothings = []

		self.matrix = [[random.gauss(0,0.2)*rmax]for y in xrange(int(self.h)) for x in xrange(int(self.w))]
		
		for x in xrange(smoothings):
			self.smooth()
		print self.matrix

	def smooth(self):
		self.smoothings.append(self.matrix[:])
		for x in xrange(int(self.w)):
			for y in xrange(int(self.h)):
				pass

	def resize(self):
		pass

	def get_value(self, x, y):
		h = 0
		for mx in xrange(int(x)):
			h+=self.matrix[int(x)][0]
		for my in xrange(int(y)):
			try:
				h+=self.matrix[int(x)][int(y)]
			except :
				pass
		print x,y,h
		return h
		

