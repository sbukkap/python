''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    num=int(input())
    def isprime(n):
            if n<=1:
                return False
            for i in range(2,n):
                if n%i == 0:
                    return False
            return True
    for i in range(num):
        LR = list(map(int,input().strip().split()))
        int1=LR[0]
        int2=LR[1]
        nums=[]
        for i in range(int1,int2+1):
            if isprime(i):
                nums.append(i)
                break
        for i in range(int2,int1,-1):
            if isprime(i):
                nums.append(i)
                break
        n=len(nums)
        if n>1:
            print(max(nums)-min(nums))
        elif n==0:
            print(-1)
        else:
            print(0)
 # Write code here

main()
