def insert(self, l: List[List[int]], nl: List[int]) -> List[List[int]]:
        final_list=[]
        for i,j in l:
            if j < nl[0]: #no overlap
                final_list.append([i,j])
            elif nl[1] < i: #no overlap and the list(i,e nl or newinterval list) is present before [i,j].Also in this case....the nl value will change
                final_list.append(nl)
                nl=[i,j]
            else:       #perfect overlap condition i.e if the above two are not true and the condition reches here then we can assure that the lists are overlapping...Then in this case...we will change the values of nl[0] and nl[1]
                nl[0],nl[1]=min(i,nl[0]),max(j,nl[1])
        final_list.append(nl)
        return final_list
