string=str(input())
no_of_elements=int(input())
num_of_a_in_the_first_two_letters=0
remainder=no_of_elements%len(string)
result=0
if string.count('a')!=0:
    for i in string[0:remainder]:
        if i=='a':
            num_of_a_in_the_first_two_letters+=1
        
    result=((no_of_elements//len(string))*string.count('a'))+num_of_a_in_the_first_two_letters

    

    
else:
    result=0
print(result)    

