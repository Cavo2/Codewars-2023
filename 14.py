# 14

def func ():
    arry = []
    shiftSpaces = 0

    while True:
        value = input( 'Enter a value: ' )
        if value == '#':
            break
        elif value.isdigit():
            shiftSpaces = int( value )
        elif type( value ) == str: 
            arry.append( value )
    result = arry[ shiftSpaces: ] + arry[ :shiftSpaces ]

    print( '\n'.join( result ) )

func()
