from prompt_toolkit import prompt
from view_func import *
from inquisitor import *

'''
	Practice contains the loop to practice translation from
	and to the foreign language. It it given an Inquisitor object
	and a number of questions to ask.
'''
def practice (inquisitor, nr_words):
	
	print ("---------------------------------------------------")
	print ("Press (enter) to continue after checking the answer")
	print ("Type (q) to stop practicing at any time")
	print ("---------------------------------------------------\n")
	
	# Variables to keep track of score and previously seen words
	correct = 0
	
	for _ in range(nr_words):
		
		# Get question from Inquisitor and ask
		(question, target) = inquisitor.get_question()
		print (question)

		# Get user answer (and check is termination command)
		answer = prompt('A: ').strip()
		if (answer.upper() == "Q"):
			clean_window(7)
			return
		
		# If answer was correct, add to score
		if len(answer) > 0 and match(answer, target):
			correct += 1
			confirm = input("Correct answer ")		
			
		# else show intended answer
		else:
			confirm = input("Incorrect, the right answer was: {0} ".format(target))
		
		# As always check if termination command was issued
		if confirm.upper() == "Q":
			clean_window(8)
			return
		
		# Clean window for next question
		clean_window(3)
	
	# Provide overview of performance then ask if should repeat
	repeat = prompt("This completes the practice.\nYou answered {0} out of {1} correctly. Repeat? (Y/n) ".format(correct, nr_words)).strip()
	clean_window(7)
	if (repeat.upper() == "Y"):
		practice(inquisitor, nr_words)
	else:
		return
	
	
	
	
'''
	Checks whether the answer matches the target.
	Includes a check if optional properties of a word
	were included in the answer or not.
'''
def match (answer, target):		
	return match_recur(answer, 0, target, 0)
	
def match_recur(answer, index_a, target, index_t):
	# Case: both reached the end without error (so match),
	# or one reached the end and the other did not (no match),
	# excepting when the target still had a bracket left to clear
	if (index_a >= len(answer)) and (index_t >= len(target)):
		return True
	
	elif (index_t >= len(target)):
		return False

	# Case: brackets in target, skip these and flip must_match
	elif (target[index_t] == '(') or (target[index_t] == ' ' and target[index_t+1] == '('):
		incr = 1
		while target[index_t + incr] != ')':
			incr += 1
	
		return (match_recur(answer, index_a, target, index_t+incr) or
				match_recur(answer, index_a, target, index_t+1))

	
	elif (target[index_t] == ')'):
		return match_recur(answer, index_a, target, index_t+1)


	# Error since they differ at index
	elif answer[index_a] != target[index_t]:
		return False

	# Final, nothing happens base case
	else:
		return match_recur(answer, index_a+1, target, index_t+1)



















