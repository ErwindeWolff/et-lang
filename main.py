from practice_guide import practice
from inquisitor import *
import file_manager as fm

terms = fm.collect_terms("word_list.txt")
inquisitor = Inquisitor(terms, mode="MIXED")
practice(inquisitor, 20)

