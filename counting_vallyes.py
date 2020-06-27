no_of_steps=int(input())
steps=str(input())
level=0
no_of_vallies=0
for step in steps:
    if step=='U':
        level+=1
    elif step=='D':
        level-=1
    if step=='U' and level==0:
        no_of_vallies+=1
print(no_of_vallies)
    
