import math as m
def isprime(n):
    s=int(sqrt(n))
    if n==1:
        return 0
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def count(n,data):
    k=[]
    for i in data:
        if isprime(i):
            k.append(i)
    return k
n=int(input())
data=list(map(int,input().split()))
primes=count(n,data)
print(*primes)
