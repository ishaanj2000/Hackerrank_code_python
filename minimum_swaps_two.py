no_of_elements=int(input())
swaps=0
unordered_array=list(map(int, input().split(" ",no_of_elements)))
while i < len(unordered_array):
    if unordered_array[i] != i + 1:
        while unordered_array[i]!=i+1:
            temp=0
            temp = unordered_array[unordered_array[i] - 1]
            unordered_array[unordered_array[i] - 1] = unordered_array[i]
            unordered_array[i] = temp
            swaps+= 1 
    i+=1
print(swaps)
        
#starting from the left
#swap the element in the wrong place 
#with the element in the place that it should be 
#increase the number of swaps each time 
#there is a swap
#print the number of swaps
