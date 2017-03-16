#
# 	Author: Ruby Abrams
# 	Descriptions:
# 			This script will output the set of pairs of integers
# 			that solve the the equation m*m + n*n = k for given
# 			command line argument integer k.
#

import sys
import numpy as np
# # turtle graphics can be used to plot the integer solutions
# # to the equation m*m + n*n = k
# import turtle
import matplotlib.pyplot as plt		# better form of plotting

def main(k):
	if float(k) < 0 or float(k) != int(k):
		print("The input is not a positive integer")
		return

	# find the set of 2-tuples whose sum of squares equals k
	forms = np.array([(a,b) for a in xrange(int(k)) for b in xrange(int(k)) if a**2+b**2 == int(k) ])
	for x,y in forms:
		color_vec = (1-(float(x)/float(k))**(.5),1-(float(x)/float(k))**(.5), 0)
		pnts = plt.plot(x,y,'o')
		plt.setp(pnts, color=color_vec)
	# plt.plot(forms)


if __name__ == '__main__':
	# main(sys.argv[1])
	for m in range(int(sys.argv[1])):
		main(m)
	plt.axis([0, 10, 0, 10])
	plt.xlabel('n')
	plt.ylabel('m')
	plt.title('Solutions to $m^2 + n^2 = k$ up to $k=$'+sys.argv[1])
	plt.show()
