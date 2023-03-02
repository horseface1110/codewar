def persistence(n):
    times = 0
    main_ = n
    tmp = 0
    while(main_ // 10):
        main_ = mutiple(main_)
        times = times + 1
    return(times)
    
def mutiple(m):
    if(m // 10 > 0):
        print(m)
        return((m % 10) * mutiple(m // 10))
    else:
        return(m % 10)
