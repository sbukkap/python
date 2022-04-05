def trap(s):
    max_pillarh=0
    length=len(s)
    for i in range(length):
        max_pillarh=max(s[i],max_pillarh)
    max_pillar_index=s.index(max_pillarh)
    total_water=0
    i=0
    pillar_start=0
    pillar_end=0
    while i<max_pillar_index:
        count=-1
        while s[pillar_start]>=s[pillar_end]:
            pillar_end+=1
            count+=1
        residue=0
        for i in range(pillar_start+1,pillar_end):
            residue+=s[i]
        total_water+=(min(s[pillar_start],s[pillar_end])*count)-residue
        pillar_start=pillar_end
        i=pillar_end
    i=length-1
    pillar_start=length-1
    pillar_end=length-1
    while i>max_pillar_index:
        count=-1
        while s[pillar_start]>=s[pillar_end]:
            pillar_end-=1
            count+=1
        residue=0
        for i in range(pillar_end+1,pillar_start):
            residue+=s[i]
        total_water+=(min(s[pillar_start],s[pillar_end])*count)-residue
        pillar_start=pillar_end
        i=pillar_end
    return total_water
print(trap([2,0,2]))
