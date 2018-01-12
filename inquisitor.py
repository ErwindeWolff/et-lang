from terms import *
from random import shuffle, random

class Inquisitor():

	def __init__(self, queries, scores, mode="FROM-TO", hist_size=20):
	
		self.queries = queries
		self.probs = self.process_scores(scores)
		
		self.mode = mode
		
		self.history = list()
		self.hist_size = hist_size
		
		
	def process_scores(self, scores):
	
		probs = []
		for q in self.queries:
			(n, s) = scores[q.fro]
			if n > 0:
				probs.append(1/(n * (s/n) + 1))
			else:
				probs.append(1)
		
		norm_const = sum(probs)
		probs = [p/norm_const for p in probs]
		
		return probs
	
		

	def get_question(self):
	
		# Draw random question that 
		# is not in recent history
		choice = self.draw_random_question()
		while (choice in self.history):
			choice = self.draw_random_question()
	
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
		
		
		

	def draw_random_question(self):
		
		# Baseline case
		choice = self.queries[0]
		
		# Select random from list based in score
		rand_val = random()
		for q, p in zip(self.queries, self.probs):
			if p >= rand_val:
				return q
			else:
				rand_val -= p
		return choice
		
		
		
		
		
		
		
