from datetime import datetime
from datetime import timedelta
dict={0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6:"Sun"}

def isprime(n):
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
prime_numbers = []
def allprimes(lim):
    for i in range(2, lim + 1):
        if isprime(i) == True:
            prime_numbers.append(i)
allprimes(365)

d, week, n= map(str, input().split())

d=datetime.strptime(d, "%Y%m%d")

numdays=-1
nn = False
for i in prime_numbers:
    diff = timedelta(i)
    actual_date = d + diff
    dtermine = dict[actual_date.weekday()]
    if isprime(actual_date.month) and dtermine==week:
        numdays=i
        break
if numdays==-1 and not nn:
    print(f"No {0}")
    nn = True
elif numdays<=int(n):
    print(f"Yes {numdays}")
else:
    print(f"No {numdays}")
