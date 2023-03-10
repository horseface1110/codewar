def productFib(prod):
    print(prod)
    root = float(prod ** (1/2))
    a = 1
    first = 0 
    second = 1 
    third = 1
    while(first * second <= prod):
        if(first * second == prod):
            return([first , second ,True])
        first = second
        second = third
        third = first + second
        #a = a + 1
        #first = Fib(a - 1)
        #second = Fib(a)
    print([first ,second,False])    
    return([first , second ,False])
  

