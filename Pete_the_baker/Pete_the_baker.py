def cakes(recipe, available):
    min = 999
    for i in recipe:
        if(available.get(i) == None):
            return(0)
        elif(available.get(i) != None and min > available.get(i) // recipe.get(i)):
                min = available[i] // recipe[i]
                print(min)
    return(min)

