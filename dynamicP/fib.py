# #  print the nth fibanocci number using optimised recursive dynamicP approach
#
# def fib(n,d):
#     if n in d:
#         return d[n]
#     if n<=2:
#         return 1
#     else:
#         val = fib(n-1,d) + fib(n-2,d)
#         d[n] = val
#         return val
# #TC -> O(n)
# #SC -> O(n)
# print(fib(5,{}))
# print(fib(10,{}))
# print(fib(50,{}))
# print(fib(55,{}))
# print(fib(500,{}))

#tabulation
def fib(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(len(dp)-2):
        dp[i+2] = dp[i]+dp[i+1]
    return dp[n]
print(fib(100))
