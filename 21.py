# 21

def func ():
    textInput = input()
    splitedText = list( textInput )
    num = 0
    counter = 0
    for e in splitedText: 
        if e.isdigit() and num == 0:
            num = int( e )
        elif e == '#' and num != 0:
            counter += 1 
        elif e.isdigit() and num != 0:
            num = num + int( e )
            if counter == 3 and num == 10: return print( True )
    return print( False )
    
func ()

            