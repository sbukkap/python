f = open("C:/Users/iamop/OneDrive/Desktop/AOC/input7.txt","r")

x = f.read().split(',')

x = [int(i) for i in x]


"""x.sort()

median = x[len(x)//2]

s = sum([abs(i - median) for i in x])

print(s)
"""
"""part two"""
def gaussian_sum(n):
    """Implementing the formula Gauss discovered
    to add all integers upto N, `explanation here.
    <https://letstalkscience.ca/educational-resources/backgrounders/gauss-summation>`_
    """
    return n * (n+1) // 2
min_fuel_cost = float("inf")
min_point = 0
for i in range(max(x)+1):
    fuel_cost = sum([gaussian_sum(abs(point-i)) for point in x])
    if fuel_cost < min_fuel_cost:
        min_fuel_cost = fuel_cost
        min_point = i
print(min_fuel_cost)
