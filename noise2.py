import numpy as np
import math
import time
import matplotlib.pyplot as plt
from scipy.stats import poisson
from multiprocessing import Process
import random
import datetime

# Lambda value for Poission distribution
lmd = 5

# Generate primes the 'stupid way'
def generate_primes(p):
	primes = []

	for possiblePrime in range(2, p):
	    
	    # Assume number is prime until shown it is not. 
	    isPrime = True
	    for num in range(2, possiblePrime):
	        if possiblePrime % num == 0:
	            isPrime = False
	      
	    if isPrime:
	        primes.append(possiblePrime)
	return primes

# run generate primes with Possion arrival interval times
def job(lmd, d):
	while 1:
		s = poisson.rvs(lmd, size=1)
		print('This is thread:', d)
		time.sleep(s)
		# t0 = datetime.datetime.now()
		print(generate_primes(random.randint(5000,10000)))
		# diff = datetime.datetime.now() - t0
		# print(diff)

# Start two processes
Process(target=job, args=(lmd,1)).start()
Process(target=job, args=(lmd,2)).start()
