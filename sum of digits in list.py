from math import*
def sums(n):
    s=0
    while n:
      r=n%10
      n=n//10
      s=s+r
    return s
def sumofdigit(n,data):
    for i in range(len(data)):
        data[i]=sums(data[i])
    return data
n=int(input())
data=list(map(int,input().split()))
sumofdigit(n,data)
print(*data)
