k=5
i=0
while k<=25:
    j=k
    if j%2==1:
        i=i+1
        while i<=k:
            print (i,end="")
            i=i+1
    while j>i:
        print (j,end="")
        j=j-1
    print("\n")
    i=k
    k=k+5
    
