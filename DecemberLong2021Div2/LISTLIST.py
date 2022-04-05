# cook your dish here
from collections import Counter
for i in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    def work():
        d = Counter(arr)

        if len(d) == 1:
            return 0
        if max(d.values())<2:
            return -1

        op = 0
        max_count_of_an_element = 0
        for i in d:
            max_count_of_an_element = max(max_count_of_an_element,d[i])
        done = False
        for i in d:
            if d[i] == max_count_of_an_element and done == False:
                op+=1
                done = True
            else:
                op+=d[i]
        return op

    print(work())

    
