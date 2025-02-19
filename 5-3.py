t=int(input("enter the number of testcases :"))
import itertools
while(t>0):
    w=input("enter the word :")
    w=tuple(w)
    k=list(sorted(w))
    G=[]
    l=itertools.permutations(k)
    for g in l:
        if(w<g):
            g=list(g)
            break
    if(type(g)==tuple):
        print("no answer")
    else:
        for i in range(0,len(k)):
            g[0]+=g[i]
        print(g[0][1:])
    t-=1