import shapefile
import random

import uuid

import scipy
import scipy.spatial
import geojson

class CityGenerator(object):
	def __init__(self, filename):
		self.filename = filename
	def open(self):
		g = shapefile.Reader(self.filename)
		self.cities = g.shapeRecords()

	def generate(self):
		for city in self.cities:
			print city.record
			point = city.shape.points[0]
			print point
			size = (1+city.record[3])*0.001
			points = (1+city.record[3])*2000
			generations = (1+city.record[3])
			
			m = 1000000.0

			g = shapefile.Writer(shapefile.POLYGON)
			g.field('building_type', 'C', 100)
			g.field('size', 'N', 2)
			
			BBW = point[0]-size
			BBE = point[0]+size
			BBN = point[1]+size
			BBS = point[1]-size

			data =[[random.randint(int(BBW*m),int(BBE*m))/m, random.randint(int(BBS*m),int(BBN*m))/m] for i in xrange(points)]
			for ring in self.voronoize(data):
				g.poly(parts=[ring])
				g.record(random.choice(['house', 'house', 'house', 'church', 'govmt']), random.randint(0,4))
			g.save('cities/'+city.record[2])

	#def generate_city(self, center, generations = None):




	def voronoize(self, data):
		print "data loaded"
		print len(data)
		v = scipy.spatial.Voronoi(data)
		print "voronoised"
		r = [vs for vs in v.regions if all([a>=0 for a in vs]) and len(vs) > 2]
		r = [[v.vertices[p] for p in a] for a in r]
		print len(r)
		selector = []
		percentage = random.uniform(0.4, 0.6)

		print percentage

		for i in xrange(len(r)):
			gauss =  random.gauss(0.4, 0.2)
			ra = random.random()
			#if gauss <  percentage and gauss > 0.3:
				#if ra<percentage:
			selector.append((i, gauss, ra))
		print len(selector)
		selected = []

		for i in selector:
			selected.append(r[i[0]])
		print len(selected)
		for r in selected:
			end = r[0]
			ring = []
			for p in r:
				ring.append([p[0],p[1]])
			ring.append([end[0], end[1]])
			yield ring


c = CityGenerator('citi_point')
c.open()
c.generate()