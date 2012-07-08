import prime

sideLength = 1 
prev = 1
total = 1
primeCount = 0

from IPython.Debugger import Tracer; 
import IPython.ipapi
IPython.ipapi.make_session()
debug_here = Tracer(); debug_here() 

while True:
	sideLength += 2
	corners = [prev + i * (sideLength - 1) for i in range(1,5)]
	primeCount += len([i for i in corners if prime.isPrime(i)])
	total += 4
	if (total > 10 * primeCount): 
		print sideLength
		break
	prev = corners[-1]

