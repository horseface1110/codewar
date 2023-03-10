def rgb(r, g, b):
    main_=[r,g,b]
    for i in range(0,3,1):
        if(main_[i] > 255):main_[i] = 255
        elif(main_[i] < 0): main_[i] = 0
    return("{}{}{}".format(hex(main_[0])[2:].zfill(2).upper(),hex(main_[1])[2:].zfill(2).upper(),hex(main_[2])[2:].zfill(2).upper()))
