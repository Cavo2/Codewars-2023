def func ():
    inputText = input( 'Enter text: ' )
    result = inputText.replace( 'a', '*' ).replace( 'e', '*' ).replace( 'i', '*' ).replace( 'o', '*' ).replace( 'u', '*' )
    result = result.replace( 'A', '*' ).replace( 'E', '*' ).replace( 'I', '*' ).replace( 'O', '*' ).replace( 'U', '*' )
    print( result )

func()