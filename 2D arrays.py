s=[]
array=[input().split(" ") for i in range(6)]
for i in range(6):
    for j in range(6):
        array[i][j]=int(array[i][j])
for i in range(4):
    for j in range(4):
        s.append(array[i][j]+array[i][j+1]+array[i][j+2]+array[i+1][j+1]+array[i+2][j]+array[i+2][j+1]+array[i+2][j+2])
print(max(s))
