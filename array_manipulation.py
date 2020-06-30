n, m=map(int, input().split(" ",2))
array=[0 for i in range(n)]
operations=[input().split(" ", 3) for i in range(m)]
a=[]
b=[]
k=[]
#convert the element to int form
for i in range(m):
    for j in range(3):
        operations[i][j]=int(operations[i][j])

#check for conditions and assign
j=0
for i in range(m):
    a.append(operations[i][j])
    b.append(operations[i][j+1])
    k.append(operations[i][j+2])
        
#assigning the operation

for i in range(m):
    for x in range(1, n+1):
        if x in range(a[i],b[i]+1):
            array[x-1]+=k[i]
            


print(max(array))
