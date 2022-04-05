def insertionSort(l):
   for index in range(1,len(l)):

     currentvalue = l[index]
     position = index

     while position>0 and l[position-1]>currentvalue:
         l[position]=l[position-1]
         position = position-1

     l[position]=currentvalue

l= [14,46,43,27,57,41,45,21,70]
insertionSort(l)
print(l)
