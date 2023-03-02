def delete_nth(order,max_e):
    main = {"i":0}
    a = list()
    for i in order:
        if(main.get(i) == None):
            main[i] = 1
            a.append(i)
        elif(main.get(i) < max_e):
            main[i] = main.get(i) + 1
            a.append(i)
    return(a)
