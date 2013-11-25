import random
import math
import uuid

def classify(attitude, mind_function, soul_function, lifestyle, limit=0.2):
	if (attitude < -limit):
		if   (mind_function < -limit and soul_function < -limit and lifestyle < -limit):
			return "SAGE INFORMANT"
		elif (mind_function < limit  and soul_function < -limit and lifestyle < -limit):
			return ""
		elif (mind_function > limit  and soul_function < -limit and lifestyle < -limit):
			return "SCIENTIST"
		elif (mind_function < -limit and soul_function < limit  and lifestyle < -limit):
			return "SENSITIVE LEADER"
		elif (mind_function < limit  and soul_function < limit  and lifestyle < -limit):
			return "LEADER"
		elif (mind_function > limit  and soul_function < limit  and lifestyle < -limit):
			return "CHAOTIC LEADER"
		elif (mind_function < -limit and soul_function > limit  and lifestyle < -limit):
			return ""
		elif (mind_function < limit  and soul_function > limit  and lifestyle < -limit):
			return ""
		elif (mind_function > limit  and soul_function > limit  and lifestyle < -limit):
			return ""
		elif  (mind_function < -limit and soul_function < -limit and lifestyle < limit):
			return ""
		elif  (mind_function < limit  and soul_function < -limit and lifestyle < limit):
			return ""
		elif  (mind_function > limit  and soul_function < -limit and lifestyle < limit):
			return ""
		elif  (mind_function < -limit and soul_function < limit  and lifestyle < limit):
			return ""
		elif  (mind_function < limit  and soul_function < limit  and lifestyle < limit):
			return ""
		elif  (mind_function > limit  and soul_function < limit  and lifestyle < limit):
			return ""
		elif  (mind_function < -limit and soul_function > limit  and lifestyle < limit):
			return ""
		elif  (mind_function < limit  and soul_function > limit  and lifestyle < limit):
			return ""
		elif  (mind_function > limit  and soul_function > limit  and lifestyle < limit):
			return ""
		elif  (mind_function < -limit and soul_function < -limit and lifestyle > limit):
			return ""
		elif  (mind_function < limit  and soul_function < -limit and lifestyle > limit):
			return ""
		elif  (mind_function > limit  and soul_function < -limit and lifestyle > limit):
			return ""
		elif  (mind_function < -limit and soul_function < limit  and lifestyle > limit):
			return ""
		elif  (mind_function < limit  and soul_function < limit  and lifestyle > limit):
			return ""
		elif  (mind_function > limit  and soul_function < limit  and lifestyle > limit):
			return ""
		elif  (mind_function < -limit and soul_function > limit  and lifestyle > limit):
			return ""
		elif  (mind_function < limit  and soul_function > limit  and lifestyle > limit):
			return ""
		elif  (mind_function > limit  and soul_function > limit  and lifestyle > limit):
			return ""
	elif (attitude > -limit and attitude < limit):
		if (mind_function < -limit  and soul_function < -limit and lifestyle < -limit):
			return "SAGE"
		elif (mind_function < limit and soul_function < -limit and lifestyle < -limit):
			return ""
		elif (mind_function > limit and soul_function < -limit and lifestyle < -limit):
			return ""
		elif (mind_function < -limit and soul_function < limit and lifestyle < -limit):
			return "WHITE KNIGHT"
		elif (mind_function < limit and soul_function < limit  and lifestyle < -limit):
			return "KNIGHT"
		elif (mind_function > limit and soul_function < limit  and lifestyle < -limit):
			return "MERCENARY"
		elif (mind_function < -limit and soul_function > limit and lifestyle < -limit):
			return "SAGE INTELLIGENCE DRIVEN COUNCELLOR"
		elif (mind_function < limit and soul_function > limit  and lifestyle < -limit):
			return "FUNNY SOCIALLY AWARE "
		elif (mind_function > limit and soul_function > limit  and lifestyle < -limit):
			return ""
	elif (attitude > limit ):
		if (mind_function < -limit and soul_function < -limit  and lifestyle < -limit):
			return "HERMIT"
		elif (mind_function > limit and soul_function < -limit and lifestyle < -limit):
			return ""
		elif (mind_function < limit and soul_function < -limit and lifestyle < -limit):
			return ""
		elif (mind_function < -limit and soul_function < limit and lifestyle < -limit):
			return "BUREAUCRAT"
		elif (mind_function < limit and soul_function < limit  and lifestyle < -limit):
			return "FUNNY SOCIALLY AWARE "
		elif (mind_function > limit and soul_function < limit  and lifestyle < -limit):
			return ""
		elif (mind_function < -limit and soul_function > limit and lifestyle < -limit):
			return "SAGE INTELLIGENCE DRIVEN COUNCELLOR"
		elif (mind_function < limit and soul_function > limit  and lifestyle < -limit):
			return "FUNNY SOCIALLY AWARE "
		elif (mind_function > limit and soul_function > limit  and lifestyle < -limit):
			return ""
	return ""



class Person(object):
	__slots__ = ['attitude', 'mind_function', 'soul_function', 'lifestyle', 'choices', 'race']
	def __init__(self, race=0, mean_mind_function=0, mean_soul_function=0, mean_lifestyle=0, move=1):
		self.attitude = random.uniform(-1,1)
		self.mind_function = random.uniform(mean_mind_function-move,mean_mind_function+move)
		self.soul_function = random.uniform(mean_soul_function-move,mean_soul_function+move)
		self.lifestyle = random.uniform(mean_lifestyle-move,mean_lifestyle+move)
		self.race = race
		self.choices = random.uniform(-1,1)

	def attitude_str(self):
		if self.attitude < -0.2:
			return "extraverted"
		elif self.attitude <0.2:
			return "neutral"
		else:
			return "introverted"

	def mind_function_str(self):
		if self.mind_function < -0.2:
			return "sensing"
		elif self.mind_function <0.2:
			return "neutral"
		else:
			return "intuitive"

	def soul_function_str(self):
		if self.soul_function < -0.2:
			return "thinking"
		elif self.soul_function <0.2:
			return "neutral"
		else:
			return "feeling"

	def lifestyle_str(self):
		if self.lifestyle < -0.2:
			return "judging"
		elif self.lifestyle <0.2:
			return "neutral"
		else:
			return "perceptive"


	def __str__(self):
		return """>>PERSON: %s\nattitude:%s \nmind functions:%s \nsoul functions:%s \nlifestyle:%s""" % ( classify(self.attitude, self.mind_function, self.soul_function, self.lifestyle), self.attitude_str(),self.mind_function_str(),self.soul_function_str(),self.lifestyle_str())

class World(object):
	__slots__ = ["societies", "starting_population", "generation"]
	def __init__(self, starting_population=100, races=[0]):
		self.societies = [Society(starting_population, races=[x]) for x in races]
		self.starting_population = starting_population
		self.generation = 0

	def step(self, delta):
		for society in self.societies:
			society.apply_delta(delta(society.total_population))

		self.generation+=1
		prev_gen = self.societies[:]
		self.societies = []
		outlying_groups = []
		for p_society in prev_gen :
			if p_society.total_population > 0:
				society = p_society.step()
				outliers = society.peek_outliers()
				if len(outliers) > society.total_population*0.1:
					outliers = society.pop_outliers()
					os = Society.from_outliers(outliers, races=society.races)
					os.set_parent(society, self.generation)
					outlying_groups.append(os)
				self.societies.append(society)
		og = outlying_groups[:]
		for outlier in og:
			for society in self.societies:
				if society.check_acceptance(outlier):
					society.accept(outlier)
					outlying_groups.remove(outlier)
		for outlier in outlying_groups:
			self.societies.append(outlier)
	def world_population(self):
		return sum([x.total_population for x in self.societies])

	def cities(self):
		return [[x.id, x.total_population, x.races] for x in self.societies]

	def races(self):
		return len(set([x.races for x in self.societies]))

	def civilize(self, races=[0]):
		self.societies.extend([Society(self.starting_population, races=[x]) for x in races])




class Society(object):
	__slots__ = ['id', 'population','permeability', 'total_population', 'parent', 'split_generation', 'races', 'deltas', 'communication_speed', 'mean_attitude', 'mean_lifestyle', 'meta_level', 'mean_mind_function', 'mean_soul_function', 'radicalization_step', 'tech_level', 'exploration_level' ]
	@classmethod
	def from_outliers(self, outliers, permeability=0.5, communication_speed=0.1, races=[0]):
		s = Society(permeability=permeability, communication_speed=communication_speed, races=races, population=outliers)
		s.radicalize()
		s.permeability = s.mean_attitude
		return s

	def set_parent(self, society, generation):
		self.parent = society
		self.split_generation=generation


	def get_split_generation(self):
		return self.split_generation

	def get_parent_tree(self):
		ret = []
		up = self.parent
		while up != None:
			ret.append(self.parent)
			up = up.parent
		return ret

	def accept(self, society):
		print "ACCEPT"
		self.population.extend (society.population)
		self.total_population = len(self.population)
		self.races = list(set([x.race for x in self.population]))
		self.permeability = float(self.permeability*len(self.races))
		self.radicalize()

	def check_acceptance(self, society):
		a = abs(self.split_generation - society.split_generation) <10
		b = society.parent in self.get_parent_tree()
		c = abs(self.mean_mind_function-society.mean_mind_function)<self.permeability /(len(society.races)+1)
		d = abs(self.mean_soul_function-society.mean_soul_function)<self.permeability /(len(society.races)+1)
		e = abs(self.mean_lifestyle-society.mean_lifestyle)<self.permeability / (len(society.races)+1)
		return ( a and b and c and d and e ) 

	def step(self):
		s = Society(initial_population=self.total_population, permeability = self.permeability, communication_speed = self.communication_speed, races = self.races, uuid=self.id, population = self.population)
		s.parent = self
		s.meta_level = self.meta_level
		s.tech_level = self.tech_level
		s.exploration_level = self.exploration_level
		s.radicalize()
		return s

	def __init__(self, initial_population=100, permeability=0.5, communication_speed=0.1, races=[0], uuid=uuid.uuid4(), population=None):
		self.id = uuid
		self.parent = None
		self.races = races
		self.deltas = []
		self.split_generation = 0
		if population is None:
			self.total_population = initial_population
			self.population =[Person(race = random.choice(self.races)) for x in range(self.total_population)]
		else:
			self.population = population
			self.total_population = len(self.population)
		self.permeability = permeability
		self.communication_speed = communication_speed

		self.mean_attitude = sum([x.attitude for x in self.population])/len(self.population)
		self.mean_mind_function = sum([x.mind_function for x in self.population])/len(self.population)
		self.mean_soul_function = sum([x.soul_function for x in self.population])/len(self.population)
		self.mean_lifestyle = sum([x.lifestyle for x in self.population])/len(self.population)

		self.radicalization_step = 0.001
		self.meta_level = 0
		self.tech_level = 0
		self.exploration_level = 0

	def __str__(self):
		s = str('\n'.join([str(x) for x in self.population]))
		return s
	
	def science_delta(self, delta):
		'''delta based on science level. This advances as soon as enough scientists are in the city.'''
		sci = len([x for x in self.population if classify(x.attitude, x.mind_function, x.soul_function, x.lifestyle) == "SCIENTIST"])
		#print sci
		if delta.name == "PLAGUE":
			if random.uniform(0, sci*self.meta_level) > sci*self.meta_level*0.9:
				delta = GenerationDelta()
		if sci > self.total_population * (0.1 + (self.tech_level / 10)):
			print "SCI_UP"
			delta.growth_rate *= random.uniform(1.1, 2.5)
			self.meta_level +=1
		pass

	def tech_delta(self, delta):
		'''delta based on tech level. This advances as soon as enough inventors are in the city.'''
		sci = len([x for x in self.population if classify(x.attitude, x.mind_function, x.soul_function, x.lifestyle) == "INVENTOR"])
		#print sci
		if sci > self.total_population * (0.1 + (self.meta_level / 10)):
			print "TECH UP"
			self.tech_level +=1
		pass

	def commerce_delta(self):
		#commerce is a typically geographic relationship
		pass

	def apply_delta(self, delta):
		self.science_delta(delta)
		self.tech_delta(delta)
		ot = self.total_population
		self.total_population = int(self.total_population *delta.growth_rate)-1
		delta = self.total_population - ot
		for x in self.population:
			if x in self.peek_outliers():
				if x.mind_function > self.mean_mind_function:
					x.mind_function += self.radicalization_step*(self.meta_level+1)
				else:
					x.mind_function -= self.radicalization_step*(self.meta_level+1)
				if x.soul_function > self.mean_soul_function:
					x.soul_function += self.radicalization_step*(self.meta_level+1)
				else:
					x.soul_function -= self.radicalization_step*(self.meta_level+1)
				if x.lifestyle > self.mean_lifestyle:
					x.lifestyle += self.radicalization_step*(self.meta_level+1)
				else:
					x.lifestyle -= self.radicalization_step*(self.meta_level+1)
			else:
				if x.mind_function > self.mean_mind_function:
					x.mind_function -= self.radicalization_step *(self.meta_level+1)
				else:
					x.mind_function += self.radicalization_step *(self.meta_level+1)
				if x.soul_function > self.mean_soul_function:
					x.soul_function -= self.radicalization_step *(self.meta_level+1)
				else:
					x.soul_function += self.radicalization_step *(self.meta_level+1)
				if x.lifestyle > self.mean_lifestyle:
					x.lifestyle -= self.radicalization_step *(self.meta_level+1)
				else:
					x.lifestyle += self.radicalization_step *(self.meta_level+1)
		if delta < 0:
			if len(self.population) + delta <4:
				self.population = []
			else:
				self.population = random.sample(self.population[:], self.total_population)	
		else:
			self.population.extend([Person(self.mean_mind_function, self.mean_soul_function, self.mean_lifestyle) for x in xrange(int(delta))])
		self.total_population = len(self.population)
		self.radicalize()

	
		'''if self.mean_mind_function<-0.8 and self.mean_soul_function <-0.8 and self.mean_attitude <-0.7:
			print "SOCIETY GETS THINKY!!!"
			self.meta_level +=1
		if self.mean_mind_function<-0.8 and self.mean_soul_function <-0.8 and self.mean_attitude <-0.7:
			print "SOCIETY GETS THINKY!!!"
			self.meta_level +=1'''

	def die(self):
		pass

	def calculate_next(self):
		self.add_generation(self.apply_delta(self.current_gen))
		self.current_gen += 1

	def mean_attitude_str(self):
		if self.mean_attitude < -0.2:
			return "extraverted"
		elif self.mean_attitude <0.2:
			return "neutral"
		else:
			return "introverted"

	def mean_mind_function_str(self):
		if self.mean_mind_function < -0.05:
			return "sensing"
		elif self.mean_mind_function <0.05:
			return "neutral"
		else:
			return "intuitive"

	def mean_soul_function_str(self):
		if self.mean_soul_function < -0.05:
			return "thinking"
		elif self.mean_soul_function <0.05:
			return "neutral"
		else:
			return "feeling"

	def mean_lifestyle_str(self):
		if self.mean_lifestyle < -0.05:
			return "judging"
		elif self.mean_lifestyle <0.05:
			return "neutral"
		else:
			return "perceptive"
	def get_winning(self):
		return [self.mean_mind_function_str(), self.mean_soul_function_str(), self.mean_lifestyle_str()]


	def peek_outliers(self, limit=0.5):
		return [x for x in self.population if math.fabs(x.mind_function - self.mean_mind_function) >limit and math.fabs(x.soul_function - self.mean_soul_function) > limit and math.fabs(x.lifestyle - self.mean_lifestyle) > limit ]

	def pop_outliers(self, limit=0.5):
		ret = [x for x in self.population if math.fabs(x.mind_function - self.mean_mind_function) >limit and math.fabs(x.soul_function - self.mean_soul_function) > limit and math.fabs(x.lifestyle - self.mean_lifestyle) > limit ]
		self.population[:] = [x for x in self.population if not(math.fabs(x.mind_function - self.mean_mind_function) >limit and math.fabs(x.soul_function - self.mean_soul_function) > limit and math.fabs(x.lifestyle - self.mean_lifestyle) > limit )]
		return ret

	def radicalize(self):
		if self.total_population > 0:
			self.mean_attitude = sum([x.attitude for x in self.population])/len(self.population)
			self.mean_mind_function = sum([x.mind_function for x in self.population])/len(self.population)
			self.mean_soul_function = sum([x.soul_function for x in self.population])/len(self.population)
			self.mean_lifestyle = sum([x.lifestyle for x in self.population])/len(self.population)
		else:
			self.mean_attitude = 0
			self.mean_mind_function= 0
			self.mean_soul_function= 0
			self.mean_lifestyle= 0

class GenerationDelta(object):

	@classmethod
	def getDelta(self, growth_rate=1.2):
		return GenerationDelta()

	@classmethod
	def nature(self, people):
		r= random.random()**people
		if r > 0.0001:
			return DisasterGenerationDelta()
		return GenerationDelta()

	def __init__(self, growth_rate=1.2):
		self.name =""
		self.growth_rate = growth_rate


class DisasterGenerationDelta(GenerationDelta):
	def __init__(self, growth_rate=0.6):
		#print "PLAGUE!!!"
		self.name ="PLAGUE"
		self.growth_rate = growth_rate

'''
s = Society()
print str(s.get_winning())
print len(s.pop_outliers())
s.radicalize()
print str(s.get_winning())
print len(s.pop_outliers())
s.radicalize()
print len(s.pop_outliers())
'''

w = World(races=['shi-kar'])
for i  in range(5):
	w.step(GenerationDelta.nature)
	print w.cities()	
w.civilize(races=['khohk'])
for i  in range(5):
	w.step(GenerationDelta.nature)
	print w.cities()
w.civilize(races=['verdi'])
for i  in range(5):
	w.step(GenerationDelta.nature)
	print w.cities()
w.civilize(races=['darwe'])
for i  in range(50):
	w.step(GenerationDelta.nature)
	print w.cities()	
