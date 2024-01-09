import string

#13

inputValue = input( 'Enter an input: ' )
inputValue = int( inputValue ) if inputValue.isdigit() else inputValue

numRefs = { index + 1: letter.upper() for index, letter in enumerate ( string.ascii_lowercase ) }
letterRefs = { letter.upper(): index + 1 for index, letter in enumerate ( string.ascii_lowercase ) }

def intFunc ( input ): 
    value = 26
    numAmount = 1
    result = []
    while value < input: 
        numAmount += 1
        value **= 2
    for i in range ( numAmount-1, -1, -1 ):
        letterPos = 1
        while letterPos*( 26**i ) <= input:
            letterPos += 1
        result.append( numRefs[letterPos-1] )
        input -= (letterPos-1)*( 26**i )
    return ''.join( map ( lambda e: e.upper(), result ) )
        
def strFunc ( input ):
    result = 0
    for i in range( len( input ) ):
        result += letterRefs[ input[ -(i+1) ].upper() ] * ( 26 ** i )
    return result 
    

def func ( input ):
    result = ''
    if type( input ) == int: 
        result = intFunc ( input )
    elif type( input ) == str:
        result = strFunc( input )
    
    print( result )

func( inputValue )