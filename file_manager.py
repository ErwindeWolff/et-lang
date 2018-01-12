from terms import Term
import os

def collect_terms(path, filename):
	terms = []
	
	if os.path.exists(path + filename):
		f = open(path + filename)
		for line in f:
			words = [x.strip() for x in line.split("\t")]
			words = [x for x in words if len(x) > 0]
			
			if len(words) >= 2:
				fro = words[0].strip()
				types = [t for t in words[1].strip()]
				term = Term(fro, types)
			
				if len(words) >= 3:
					term.to = words[2].strip()
				
				terms.append(term)
		f.close()
	return terms


def load_performance_file (path, filename, terms):
	
	scores = dict()
	if os.path.exists(path + filename):
	
		f = open(path + filename, "r+")
		for line in f:
			words = [word.strip() for word in line.split("\t")]
			words = [x for x in words if len(x) > 0]
			
			if len(words) >= 3 and words[0][0] != "%":
				scores[words[0]] = (int(words[1]), int(words[2]))
			
	else:
		f = open(path + filename, 'w')
	
	# Add unknown terms with base score
	for term in terms:
		if not (term.fro in scores):
			f.write(term.fro + "\t0\t0\n")
			scores[term.fro] = (0, 0)
		
	f.close()
	return scores
	
	
	
def modify_performance_file(path, filename, new_scores):

	f = open(path + filename, "w")
	
	f.close()



