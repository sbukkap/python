def selectionSort(l):
   for fillslot in range(len(l)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if l[location]>l[maxpos]:
               maxpos = location

       temp = l[fillslot]
       l[fillslot] = l[maxpos]
       l[maxpos] = temp
l= [14,46,43,27,57,41,45,21,70]
selectionSort(l)
print(l)
