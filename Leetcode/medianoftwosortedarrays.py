def median(list1,list2):
    merged_list=list1+list2
    merged_list.sort()
    mid=len(merged_list)/2
    if len(merged_list)%2==0:
        median=(merged_list[int(mid)]+merged_list[int(mid)-1])/2
    else:
        median=merged_list[int(mid)]

    return median
print(median([1,2,3],[5,7,8]))
