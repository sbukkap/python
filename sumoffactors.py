def sumoffactors(b):
    summ = 0
    i = 1
    for i in range(1,int(m.sqrt(b))+1):
        if b%i == 0:
            q = b // i
            summ+=i
            if q!=i:
                summ+=q
                
