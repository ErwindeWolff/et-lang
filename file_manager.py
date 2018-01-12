from terms import Term

def collect_terms(filename):
	f = open(filename)
	terms = []
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
	
