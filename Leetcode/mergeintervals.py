l=[[1,3],[5,8],[2,6],[9,10]]
"""first method"""
"""
sort the list such that the first elements in each sublist are in asc. order
this can be done using 'key' and writing a suitable function for sort() method or by using lambda func.
"""
l.sort(key=lambda i:i[0])

"""
list is now sorted as per req."""
final_list=[l[0]]

for i in range(1,len(l)):
    if final_list[-1][1] >= l[i][0]:
        x=final_list.pop()
        final_list.append([x[0][0],max(x[0][1],l[i][1]))
    else:
        final_list.append([l[i][0],l[i][1]])
print(final_list)
"""
    """
        sort the list such that the first elements in each sublist are in asc. order
        this can be done using 'key' and writing a suitable function for sort() method or         by using lambda func.
        """"""
        l.sort(key=lambda i:i[0])

        """
"""       list is now sorted as per req.""""""
        final_list=[l[0]]
        for i,j in l[1:]:
            if final_list[-1][1] >= i: #if overlapping occurs
                final_list[-1][1]=max(final_list[-1][1],j)
            else:
                final_list.append([i,j])
        return final_list"""
