# 27

def func ():
    width = int( input( 'Enter width: ' ) )
    height = int( input ( 'Enter height: ' ) )
    deep = int( input ( 'Enter deep: ' ) )
    result = []
    lateralDeep = -4
    lateralDeepSubtractOnce = True
    for i in range ( 1, deep+2 ): # Draw the box deep
        resultLength = len( result ) - 1
        startSpaces = deep+1 - i

        centerDeep = ( '_' * width ) if resultLength+1 == deep else ( ' ' * width )

        lateralDeep += 2 if resultLength <= height else 0
        if resultLength >= height and lateralDeepSubtractOnce: 
            lateralDeep -= 1
            lateralDeepSubtractOnce = False
        

        finalBar = '/' if resultLength >= height else '\\'
        if i == 1: result.append( f'{ " " * startSpaces }{ "_" * ( width+1 ) }' )
        else:
            result.append( f'{ " " * startSpaces }/{ centerDeep }/{ " " * lateralDeep }{ finalBar }' )


    for i in range ( 1, height+1 ):
        resultLength = len( result ) - 1
        startSpaces = i - 1

        centerDeep = ( '_' * width ) if i == height else ( ' ' * width )

        lateralDeep -= 0 if i == 1 else 1
        if resultLength < height: lateralDeep += 1
        if resultLength > height: lateralDeep -= 1 

        finalBar = '/' if resultLength >= height else '\\'

        result.append( f'{ " " * startSpaces }\\{ centerDeep }\\{ " " * lateralDeep }{ finalBar }' )

    print( '\n'.join( result ) )

func()
