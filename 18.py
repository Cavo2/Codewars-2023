from functools import reduce

# 18

def func ():
    result = [ 0 ]
    previousMaxWidth = 0

    while True:
        text = input()
        if text == '#': break
        text = text.split ( ' ' )
        maxWidth = reduce( lambda acc, e: len( e ) if len( e ) > acc else acc, text, 0 )

        if maxWidth > previousMaxWidth:
            result[-1] = '#'*( maxWidth+4 ) + '\n'
        else: None

        for e in text:
            result.append( '# ' + e + ( ' '*( maxWidth-len( e ) ) ) + ' #' + '\n' )

        result.append( '#'*( maxWidth+4 ) + '\n' )
        previousMaxWidth = maxWidth

    result = ''.join( result )
    print( result )

        
func()