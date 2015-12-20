"""
regex_assignment.py: Sums all the numbers in the given text and prints the result.
"""
__author__      = "Caio Albuquerque Melo"

import re
print sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_215326.txt').read())])
