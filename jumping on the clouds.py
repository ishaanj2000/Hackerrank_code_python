no_of_clouds=int(input())
cloud_list=list(map(int, input().split(" ")))
    
jumps=0
i=0
while(i<no_of_clouds-1):
    if i+2>=no_of_clouds or cloud_list[i+2]==1:
        i=i+1
        jumps=jumps+1
    else:
        i+=2
        jumps=jumps+1
print(jumps)
