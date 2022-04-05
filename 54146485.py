# cook your dish here
for i in range(int(input())):
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr.sort()
    def work(arr,n):
        sum = 0
        for i in arr:
            sum+=i
        if sum%3 != 0:
            return -1
        i = 0
        j = n - 1
        moves = 0
        while i<j:
            ri = arr[i]%3
            rj = arr[j]%3
            
            if rj == 0 and ri == 0:
                i+=1
                j-=1
            elif ri == 0 and rj!=0:
                i+=1
            elif rj == 0 and ri!=0:
                j-=1
            elif ri<rj:
                arr[i]-=1
                arr[j]+=1
                i+=1
                j-=1
                moves+=1
            elif ri > rj:
                arr[i]+=1
                arr[j]-=1
                j-=1
                i+=1
                moves+=1
            elif ri == rj and ri == 1:
                arr[i]-=1
                arr[j]+=1
                i+=1
                moves+=1
            elif ri == rj and ri == 2:
                arr[j]+=1
                arr[i]-=1
                j-=1
                moves+=1
        return moves
        
    print(work(arr,n))