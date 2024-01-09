# 24

def func ():
    dividendInput = input( 'Enter dividends: ' ).split( ' ' )
    constant = int( input( 'Enter constants inputs: ' ) )

    firstLine = '     |' + ''.join( map ( lambda e: ( 5 - len( e ) ) * ' ' + e, dividendInput ) )
    secondLine = f'    {constant}|     '
    lastLine = f'     |'

    currentValue = 0
    for pos, e in enumerate( dividendInput ):
        currentValue = currentValue + int( e )
        # whiteSpaces = 5 - len( str(currentValue) )
        lastLine = f'{lastLine}{currentValue:5d}'

        if pos + 1 >= len( dividendInput ): break 
        currentValue = currentValue * constant
        # whiteSpaces = 5 - len( str(currentValue) )
        secondLine = f'{secondLine}{currentValue:5d}'

    result = f'{firstLine} \n{secondLine} \n -------------------------- \n{lastLine}'
    print( result )


func()

