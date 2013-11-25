import scipy
import scipy.spatial
import geojson
import random

import shapefile

import noise


def voronoize(data):
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


data = shapefile.Reader("output")
data = data.shapes()
data = [d.points[0] for d in data]

oo = shapefile.Writer(shapefile.POLYGON)
oo.field('FIRST_FLD')
oo.field('height')


for ring in voronoize(data):
	oo.poly(parts=[ring])
	oo.record(str(len(ring)), random.gauss(0.5,0.2))
print 'saving'
oo.save('voro')
print "done" 		
