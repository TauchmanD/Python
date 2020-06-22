x = 1.5
result = 1.07
i = float(1)
while True:
    if (2*x+i)/(2+i) == result:
        print(i)
    elif(i > 25):
        print((2 * x + i) / (2 + i))
        break
    else:
        i += 1

