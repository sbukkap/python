
     def maxArea(self, height: List[int]) -> int:



        start_index=0
        end_index=len(height)-1
        area=0
        prev_start=0
        prev_end=0


        while(start_index!=end_index):

            if height[start_index]<prev_start:
                start_index+=1
                continue
            if height[end_index]<prev_end:
                end_index-=1
                continue

            new_area=min(height[start_index],height[end_index])*(end_index-start_index)

            if new_area>area:
                area=new_area

            if height[end_index]>height[start_index]:
                prev_start=height[start_index]
                start_index+=1
            else:
                prev_end=height[end_index]
                end_index-=1


        return area
