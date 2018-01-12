from practice_guide import practice
from inquisitor import *
import file_manager as fm

# Collect terms and filter out those without translation
terms = fm.collect_terms("", "word_list.txt")
terms = [t for t in terms if t.has_translation()]

# Load associated performance file 
# (#times_asked and #correctly_answered)
scores = fm.load_performance_file("", "word_performance.txt", terms)

#inquisitor = Inquisitor(terms, scores, mode="FROM-TO", hist_size=20)
inquisitor = Inquisitor(terms, scores, mode="TO-FROM", hist_size=20)
#inquisitor = Inquisitor(terms, scores, mode="MIXED", hist_size=20)

practice(inquisitor, 20)

