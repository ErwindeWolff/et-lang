import os

class Term():
	
	def __init__(self, fro, types):
		self.fro = fro
		self.types = types
		self.to = ''
	
	def has_translation(self):
		return len(self.to) > 0
		
	def get_word_types(self):
		s = ""
		last = len(self.types)-1
		for i, t in enumerate(self.types):
			s += self.full_type_word(t)
			if (i < last):
				s += ", "
		return s
	
	def full_type_word(self, t):
		if t == 'v':
			return 'verb'
		if t == 'n':
			return 'noun'
		if t == 'a':
			return 'adjective'
		if t == 'p':
			return 'pronoun'
		if t == 'd':
			return 'determiner'
		if t == 'r':
			return 'preposition'
		if t == 'c':
			return 'conjunction'
			
		
	def to_string(self):
		if len(self.to) > 1:		
			return self.fro + " " + "".join(self.types) + "\t" + self.to + "\n"
		else:
			return self.fro + " " + "".join(self.types) + "\n"
	
	








