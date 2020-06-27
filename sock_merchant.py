no_of_socks=int(input())
count=0
list_of_socks=list(map(int, input().split(" ", no_of_socks)))
list_of_socks.sort()
print(list_of_socks)
new=list(set(list_of_socks))
for key in new:
    c=list_of_socks.count(key)
    if c%2==0:
        count+=c//2
    elif(c%2==1):
        count+=(c-1)//2
print(count)
    
