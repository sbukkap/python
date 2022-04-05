def btod(binary):
    decimal = 0
    binary_str = str(binary)

    for i in binary_str:
        decimal = decimal*2 + int(i)
    return decimal
print(btod(10000))
