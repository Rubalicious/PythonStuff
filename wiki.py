#
# Author: Ruby Abrams
# Description:
#    A script to access summaries from wikipedia through terminal
#
import sys
import wikipedia

# I expect commands of the form:
# wiki search_term

# NEEDS WORK
search_term = sys.argv[1]
print('')
print(wikipedia.summary(search_term))
print('')
