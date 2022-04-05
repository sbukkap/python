f = open("C:/Users/iamop/OneDrive/Desktop/AOC/test5.txt","r")
x = list(map(str, f.readlines()))
fish = []
for i in x:
    fish.extend(i.split(','))
for i in range(len(fish)):
    fish[i] = int(fish[i])
c = 0

fish.sort()

days = 0

while True:
    max_elem = fish[-1]
    days+=max_elem+1
    if 256 - days>=0:
        temp = [8 - (max_elem-i) for i in fish]
        for i in range(len(fish)):
            fish[i] = 6 - (max_elem - fish[i])
        fish.extend(temp)
    else:
        max_elem = abs(256 - days + 2)
        print(len(fish)+max_elem*2)
        break
