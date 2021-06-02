def evenodd(n,data):
    e,o=0,0
    for i in data:
        if i%2==0:
            e+=1
        else:
            o+=1
    return e,o


n=int(input())
data=list(map(int,input().split()))
total=evenodd(n,data)
print(total)


    
