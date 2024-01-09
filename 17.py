# 17

def func ():
    text = input ( 'Enter the text: ' )
    text = text.split( ' ' )
    while ( True ):
        pos = input ()
        pos = int ( pos ) if pos.isdigit() else pos 
        if pos == '#': break

        word = text[ pos-1 ]
        result = word[ ::-1 ][ 1: ] + '.' if word[ ::-1 ][0] == '.' else word[ ::-1 ]
        text[ pos-1 ] = result 

    text = ' '.join( text )
    print( text )

func ()
