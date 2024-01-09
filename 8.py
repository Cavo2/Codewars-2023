def func ():
    inputNumber = int( input( 'Enter number: ' ) )
    result = [ str( inputNumber ) ]
    
    currentNumber = inputNumber
    while currentNumber != 1:
        if currentNumber % 2 == 0: currentNumber /= 2
        else: currentNumber = currentNumber * 3 + 1
        numberToAppend = str( int( currentNumber ) )
        result.append( numberToAppend )

    print( ' -> '.join( result ) + f' [{ len( result ) - 1 }]' )
    

func()