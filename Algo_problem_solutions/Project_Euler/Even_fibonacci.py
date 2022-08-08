def evenFibonacci():
    currFib = [1, 2]
    sumFib = 2
    i = 0
    while currFib[i + 1] <= 4000000:
        f = currFib[i] + currFib[i + 1]

        if f % 2 == 0:
            sumFib += f

        currFib.append(f) 
        i += 1

    print(sumFib)

evenFibonacci()
    
    