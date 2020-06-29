test_cases=int(input())
for i in range(0, test_cases):
    no_of_bribes=0
    no_of_people=int(input())
    new=[0 for k in range(no_of_people)]
    people_list=list(map(int, input().split(" ",no_of_people)))
    sorted_list= sorted(people_list)
    while people_list!= sorted_list:
        for j in range(no_of_people-1):
            if people_list[j+1]<people_list[j]:
                temp=people_list[j]
                people_list[j]=people_list[j+1]
                people_list[j+1]=temp
                no_of_bribes+=1
                new[people_list[j+1]-1]+=1
                break
            else:
                continue


    for element in new:
        if element>2:
            result=1
            break
        else:
            result=0
    if result==1:
        print("Too chaotic")
    else:
        print(no_of_bribes)
