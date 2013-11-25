import shapefile
import random

import noise
import uuid

class PointGenerator(object):
	def __init__(self, limit = 6500, BBN=90, BBS=-90, BBE=180, BBW=-180, m=1000000.0):
		self.limit = 6500
	 	self.BBN = 90
		self.BBS = -90
		self.BBE = 180
		self.BBW = -180
		self.m = 1000000.0

	def generate(filename):

		g = shapefile.Writer(shapeType=1)
		g.field('X')
		g.field('Y')
		g.field('Name', 'C', 100)
		g.field('Size', 'N', 2)


		freq_10 = 0.1
		arr = range(10)
		arr.extend(range(9))
		arr.extend(range(9))
		arr.extend(range(9))
		arr.extend(range(9))

		for i in xrange(limit):
			lon = random.randint(BBW*m,BBE*m)/m
			lat = random.randint(BBS*m,BBN*m)/m
			g.point(x=lon, y=lat)
			g.record(str(lon), str(lat), str(uuid.uuid4()), random.choice(arr))
		g.save(filename)


world = PointGenerator(limit=100000)
world.generate('output')

cities = PointGenerator(limit=6500)
cities.generate('citi_point')