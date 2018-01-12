import sys

def clean_window(nr_lines):
	for _ in range(nr_lines):
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
