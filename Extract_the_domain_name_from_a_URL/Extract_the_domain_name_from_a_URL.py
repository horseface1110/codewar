def domain_name(url):
    c = 0
    b =''
    print(url)
    url = url.replace('http://','')
    url = url.replace('https://','')
    url = url.replace('www.','')
    a = url.split('.')
    for i in a:
        if(len(i) > c and  i.find("/") == -1):
            c = len(i)
            b = i
    print(b)
    return(b)
   
