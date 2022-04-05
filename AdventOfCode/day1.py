file = open("C:/Users/iamop/OneDrive/Desktop/AOC/input.txt",'r')

arr = list(map(int, file.readlines()))
c = 0
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        c+=1
print(c)

"""part two"""
file = open("C:/Users/iamop/OneDrive/Desktop/AOC/input.txt",'r')

arr = list(map(int, file.readlines()))

currsum = 0
prevsum = 0
c = 0
windowstart = 0
for windowend in range(len(arr)):
    currsum+=arr[windowend]
    if (windowend - windowstart) == 2:
        if currsum>prevsum:
            c+=1
        prevsum = currsum
        currsum -= arr[windowstart]
        windowstart+=1
print(c-1)
