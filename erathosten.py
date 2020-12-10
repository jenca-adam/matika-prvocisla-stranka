#!/usr/bin/python
import sys,cmd,math
def primes(num):
    primes=[]
    index=2
    end=False
    primecount=0
    while True:
            i=True
            for prime in primes[:int(math.sqrt(index))+1]:
                if index%prime == 0:
                    i=False
                    break
            if i:
                primes.append(index)
                primecount+=1
                if primecount==num:
                    break
            index+=1
    return primes
def primesrange(num):
    primes=[]
    index=2
    for prime in range(num-1):
            i=True
            for prime in primes[:int(math.sqrt(index))+1]:
                if index%prime == 0:
                    i=False
                    break
            if i:
                primes.append(index)
            index+=1
    return primes

def isprime(num):
    return num in primesrange(num)
    
        
