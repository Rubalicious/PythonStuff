import sys

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1)+fib(n-2)

for i in range(int(sys.argv[1])):
	# print "the %s th term of the fibonacci sequence is %s" %(i,fib(i))
	print(str(fib(i))+" ",end='')
print()
