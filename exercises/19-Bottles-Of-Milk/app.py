 
def number_of_bottles():

    for x in range(99,-1,-1):  
        if x == 1: print(str(x) + " bottle of milk on the wall, " + str(x) + " bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.")
        elif x == 0: print("No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.")
        else: print(str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk.\nTake one down and pass it around, " + str(x-1) + " bottles of milk on the wall.")


number_of_bottles()