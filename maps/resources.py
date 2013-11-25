import random
import uuid

class ResourceGeneator(object):
	interaction_types  = [
		'EXOTERMIC',
		'ENDOTERMIC'
	]

	def __init__(self, amount, magic=0.5):
		self.amount=amount
		self.generated = []
		self.interactions = []
		self.magic = magic
	def generate(self):
		for i in xrange(self.amount):
			print i
			
			el = uuid.uuid4()
			self.generated.append(el)
			print 'name:',el

			magic = random.random() <self.magic
			print 'magic:', magic

		for i in self.generated:
			if random.choice([0,0,0,1]) == 1:
				els = [random.choice(self.generated) for e in range(random.choice([1,1,1,2,3,4]))]
				int_type = random.choice(self.interaction_types)
				mass_ratio = random.uniform(0.2, 10)
				self.interactions.append({'el':i,' els':els, 'int':int_type, 'mass_ratio':mass_ratio})
		print self.interactions

rg = ResourceGeneator(50, magic=0.1)
rg.generate()


