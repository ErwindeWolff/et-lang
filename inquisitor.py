from terms import *
from random import shuffle, random

class Inquisitor():

	def __init__(self, queries, mode="FROM-TO", hist_size=20):
	
		self.queries = [q for q in queries if q.has_translation()]
		self.mode = mode
		self.history = list()
		self.hist_size = hist_size
		

	def get_question(self):
	
		# Find a question that is not
		# in maintained history
		shuffle(self.queries)
		choice = self.queries[0]
		for q in self.queries:
			if q not in self.history:
				choice = q
				break
	
		# Update history to 
		# remember this question
		if len(self.history) >= self.hist_size:
			self.history = self.history[1::]
		self.history.append(choice)
	
		# Turn choice into target
		# and accompanying question
	
		if self.mode == "FROM-TO":
			target = choice.to
			question = "Q: " + choice.fro + " [" + choice.get_word_types() + "]"
		
		elif self.mode == "TO-FROM":
			target = choice.fro
			question = "Q: " + choice.to + " [" + choice.get_word_types() + "]"
		
		else:
			if random() > 0.5:
				target = choice.to
				question = "Q: " + choice.fro + " [" + choice.get_word_types() + "]"
			else:	
				target = choice.fro
				question = "Q: " + choice.to + " [" + choice.get_word_types() + "]"
				
		return (question, target)
