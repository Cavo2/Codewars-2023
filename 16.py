# 16

def func (): 
    text = input( 'Enter text: ' )
    splitedText = text.split( ' ' )
    uppercount = 0
    for i, e in enumerate( splitedText ):
        if e[0].isupper():
            uppercount += 1
            if uppercount > 1: splitedText[i-1] = splitedText[i-1][0]
        elif uppercount > 1: 
            splitedText[i-1] = splitedText[i-1][0]
            uppercount = 0
        else: uppercount = 0

        if i == len( splitedText ) - 1 and e[0].isupper() and uppercount > 0: # This is the last word and its part of an acronym
            splitedText[i] = splitedText[i][0]
        
    result =  ''.join( word if len( word )==1 and ( pos+1 < len( splitedText ) and len( splitedText[pos+1] )==1 ) else word + ' ' for pos, word in enumerate( splitedText ) )
    print( result )



func()