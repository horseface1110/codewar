def solution(s):
    for i in s:
        if(i.isupper() and s.find(" " + i) == -1):
            print(s.find(" " + i))
            s = s.replace(i , " " + i)
    return(s)
