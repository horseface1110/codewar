def alphabet_position(text):
    a = ""
    text = text.replace(" ","")
    text = text.lower()
    for i in text:
        if(i >= 'a'and i <= 'z'):
            a = a + str(ord(i) - 96) + " "
    return(a[:-1])   
