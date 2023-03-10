def perimeter(n):
    a , b , c = 1 , 1 , 1
    for i in range(0,n):
        a , b , i , c = b , a + b , i + 1 , c + b
    print(c)
    return(4 * c)
