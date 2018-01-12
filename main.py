from practice_guide import practice
from inquisitor import *
from terms import *
from view_func import *
import file_manager as fm

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

import time

def main():

	# Load settings of the program
	settings = dict()
	settings['show_welcome_screen'] = 1
	settings['use_numeric_menu'] = 0
	
	# Show welcome screen
	if settings['show_welcome_screen'] == 1:
		show_welcome_screen()
	
	# Load in data
	terms = fm.collect_terms("", "word_list.txt")
	
	# Open menu
	active = True
	while active:
	
		if settings['use_numeric_menu'] == 1:
			active = numeric_menu(terms, settings)
			clean_window(2)
		else:
			active = cml_menu(terms, settings)
			clean_window(4)
	clean_window(7)
	


def show_welcome_screen():

	print("\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
	print("*~                              ~*")
	print("*~ Welcome to Elder's Language! ~*")
	print("*~                              ~*")
	print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")



def cml_menu(terms, settings):

	print('Type "--help" for more information and "--quit" to exit')
	print('Type "--mode_num" to switch to a numeric menu\n')

	command = prompt('', history=FileHistory('command_history.txt'),
					auto_suggest=AutoSuggestFromHistory())
	
	# Process prompt
	words = command.split(' ')
	if words[0] == '--practice' or words[0] == '-p':
		full_terms = [t for t in terms if t.has_translation()]
		
		#####
		#####
		mode = "MIXED"
		#####
		#####
		
		start_practice(terms, mode)

	elif words[0] == '--lex_info' or words[0] == '-i':
		lexicon_info(terms)
		confirm = prompt('')
		clean_window(12)
		
	elif words[0] == '--quit' or words[0] == '-q' or words[0].upper() == 'Q':
		return False
	
	elif any(c == words[0] for c in ['--mode_num', '-m']):
		settings['use_numeric_menu'] = 1

	return True




def numeric_menu(terms, settings):

	print("Got to this mode\n")
	time.sleep(2)

	return False






def start_practice(terms, mode="MIXED"):
	# Filter terms without translation
	full_terms = [t for t in terms if t.has_translation()]

	# Load associated performance file 
	# (#times_asked and #correctly_answered)
	scores = fm.load_performance_file("", "word_performance.txt", full_terms)

	inquisitor = Inquisitor(full_terms, scores, mode=mode, hist_size=20)

	practice(inquisitor, 20)


def lexicon_info(terms):
	
	untrans = [term for term in terms if not term.has_translation()]
	trans = [term for term in terms if term.has_translation()]
	
	# v = verb (walk, sleep)
	# n = noun (dog, tree, red)
	# a = adjective (large, green)
	# p = pronoun (I, he, she, we)		
	# d = determiner (this, that, every, many etc)		
	# r = preposition (after, in, to, on, with etc)	
	# c = conjunction (and, because, but etc)
	
	print("\nThe lexicon currently contains {0} words.\nOf these words, {1} currently do not have a translation.".format(len(terms), len(untrans)))
	print("The {0} translated words contain:".format(len(trans)))
	
	print("{0} nouns".format(len([x for x in trans if 'n' in x.types])))
	print("{0} pronouns".format(len([x for x in trans if 'p' in x.types])))
	print("{0} verbs".format(len([x for x in trans if 'v' in x.types])))
	print("{0} adjectives".format(len([x for x in trans if 'a' in x.types])))
	print("{0} determiners".format(len([x for x in trans if 'd' in x.types])))
	print("{0} prepositions".format(len([x for x in trans if 'r' in x.types])))		
	print("{0} conjunctions".format(len([x for x in trans if 'c' in x.types])))



main()











