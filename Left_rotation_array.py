n, d=map(int,(input().split(" ")))
arr=list(map(int, input().split(" ")))

for j in range(d):
    first=arr[0]
    arr.remove(first)
    arr.append(first)
    
for element in arr:
    print(element, end=' ')
    
