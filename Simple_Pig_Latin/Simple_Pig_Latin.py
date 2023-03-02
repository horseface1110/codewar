def pig_it(text):
    a = ['!','?']
    str = ""
    main = list(text.split(" "))
    for i in main:
        if(not i in a):
            i = i[1:] +i[0] + 'ay'
        str = str + i + " "
    return(str[0:len(str) - 1])
