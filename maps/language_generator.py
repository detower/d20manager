import string
import itertools
import random

class Language(object):
    def __init__(self, location="CENTER", status="NEUTRAL", culture="MIDDLEAGE", society="EGO", mode="STANTIAL"):
        self.words =[]
        self.concepts = {}
        self.concepts[0] = ['BEING', 'WIND', 'BE', 'OWN', 'SUN', 'MOON', 'NOT']
        self.concepts[1] = []
        self.concepts[2] = []
        self.concepts[3] = []


        if location == "CENTER":
          self.concepts[0].extend(['SUN NEVER','SUN BORN','SUN DIES','SUN HIGH', 'WATER', 'FIRE', 'LIVE'])
          self.concepts[1].extend(['MOUNTAIN', 'RIVER'])
          self.concepts[2].extend(['SNOW', 'RAIN', 'ICE'])
        elif location == "NORTH":
          self.concepts[0].extend(['SUN BORN','SUN DIES','SUN HIGH', 'WATER', 'FIRE', 'DIE','SNOW-HARD', 'SNOW-soft', 'SNOW-heavy', 'RAIN', 'ICE'])    
          self.concepts[1].extend(['MOUNTAIN', 'RIVER', 'SEA'])
          self.concepts[2].extend(['ICEBERG'])
        elif location == "SOUTH":
          self.concepts[0].extend(['SUN BORN','SUN DIES','SUN NEVER', 'WATER', 'FIRE', 'LIVE', 'RAIN', 'SNOW'])    
          self.concepts[1].extend(['MOUNTAIN', 'RIVER', 'SEA'])
          self.concepts[2].extend(['TREE'])
        elif location == "EAST":
          self.concepts[0].extend(['SUN NEVER','SUN DIES','SUN HIGH', 'WATER', 'FIRE', 'LIVE'])
          self.concepts[1].extend(['MOUNTAIN', 'RIVER'])
          self.concepts[2].extend(['SNOW', 'RAIN', 'ICE'])
        elif location == "WEST":
          self.concepts[0].extend(['SUN NEVER','SUN BORN','SUN HIGH', 'WATER', 'FIRE', 'LIVE'])
          self.concepts[1].extend(['MOUNTAIN', 'RIVER'])
          self.concepts[2].extend(['SNOW', 'RAIN', 'ICE'])

        if status == "NEUTRAL":
          self.concepts[3].extend(['CASTLE'])
        elif status =="BELLIGERANT":
          self.concepts[3].extend(['CITY', 'TOWN', 'VILLAGE', 'CASTLE', 'WALL', 'LEAD'])
        elif status =="PEACEFUL":
          self.concepts[3].extend(['CITY', 'TOWN', 'VILLAGE'])

        if culture=="NAIF":
          self.concepts[3].extend([])
        elif culture=="MIDDLEAGE":
          self.concepts[3].extend(['RELIGION', 'GOD', 'SOUL'])
        elif culture=="MODERN":
          self.concepts[3].extend(['RELIGION', 'GOD', 'SOUL', 'SOCIETY', 'HISTORY', 'EVIL'])

        if society == "EGO":
          self.concepts[0].extend(['I'])
        elif society == "COMMERCIAL":
          self.concepts[0].extend(['I', 'YOU', 'PACT'])
        elif society == "SOCIALIST":
          self.concepts[0].extend(['YOU', 'NON-YOU'])
                
        if mode == "STANTIAL":
          self.concepts[0].extend(['CITY', 'TOWN', 'VILLAGE', 'TRAVEL'])

        elif mode == "NOMADIC":
          self.concepts[0].extend(['ENCAMPMENT', 'PLACE', 'MOVE'])
        elif mode == "SEASONAL":
          self.concepts[0].extend(['VILLAGE', 'MOVE', 'SPRING'])
        
        self.initial_consonants = (set(string.ascii_lowercase) - set('aeiou')
                          # remove those easily confused with others
                          
                          # add some crunchy clusters
                          | set(['bl', 'br', 'cl', 'cr', 'dr', 'fl',
                                 'fr', 'gl', 'gr', 'pl', 'pr', 'sk',
                                 'sl', 'sm', 'sn', 'sp', 'st', 'str',
                                 'sw', 'tr', 'bh', 'vh', 'ph', 'ss', 'qw', 'qr', 'rl'])
                          )
        self.final_consonants = (set(string.ascii_lowercase) - set('aeiou')
                        # confusable
                        
                        # crunchy clusters
                        | set(['ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt',
                               'pt', 'sk', 'sp', 'ss', 'st'])
                        )
        self.vowels = ['a','e','i','o','u', 'uo', 'ae', 'io', 'oe', 'oi', 'uoi'] # we'll keep this simple
        # each syllable is consonant-vowel-consonant "pronounceable"
        self.syllables = {}
        self.args = [self.initial_consonants, self.vowels]

        for i in xrange(len(self.concepts)):
            self.syllables[i] = {}
            for x in self.concepts[i]:
              data =  [random.choice(list(a)) for a in self.args]
              if ''.join(data) not in self.words:
                print data
                print ''.join(data)
                self.syllables[i][x] = ''.join(data)
                self.words.append(''.join(data))
            self.args.extend([self.final_consonants, self.vowels])
        
    # you could trow in number combinations, maybe capitalized versions... 

    def smooth(self, mode = "LONG"):
      for i in xrange(len(self.concepts)):
        print i
        for x in self.concepts[i]:
          print x 
          #print "S",self.syllables[i][x]
          if mode =="LONG":
            self.syllables[i][x] = self.syllables[i][x].replace('i', 'ii')
            self.syllables[i][x] = self.syllables[i][x].replace('bl', 'bal')
            self.syllables[i][x] = self.syllables[i][x].replace('br', 'bal')
            self.syllables[i][x] = self.syllables[i][x].replace('cl', 'cal')
            self.syllables[i][x] = self.syllables[i][x].replace('cr', 'cal')
            self.syllables[i][x] = self.syllables[i][x].replace('dl', 'dal')
            self.syllables[i][x] = self.syllables[i][x].replace('dr', 'dal')
          if mode == "HARDEN":
            self.syllables[i][x] = self.syllables[i][x].replace('z', 'tz')
            self.syllables[i][x] = self.syllables[i][x].replace('ch', 'k')
            self.syllables[i][x] = self.syllables[i][x].replace('c', 'k')
            self.syllables[i][x] = self.syllables[i][x].replace('r', 'dj')
            self.syllables[i][x] = self.syllables[i][x].replace('oi', 'og')
          if mode == "NASALIZE":
            self.syllables[i][x] = self.syllables[i][x].replace('og', 'ong')
            self.syllables[i][x] = self.syllables[i][x].replace('ag', 'ang')
            self.syllables[i][x] = self.syllables[i][x].replace('ok', 'onk')
            self.syllables[i][x] = self.syllables[i][x].replace('oc', 'onq')
            


    def vocabulary(self):
        return self.syllables



l = Language("NORTH", "PEACEFUL", "MODERN", "COMMERCIAL")
print l.vocabulary()
l.smooth('HARDEN')
l.smooth('LONG')
print l.vocabulary()
