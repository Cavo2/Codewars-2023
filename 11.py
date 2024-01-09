def func ():
    letters = input( 'Enter letters: ' )
    wordsAmount = int( input( 'Enter number of words: ' ) )
    words = []
    for i in range ( 0, wordsAmount ):
        word = input( 'Enter word: ' )
        words.append( word )
    
    result = []
    for e in words:
        if all( e.lower() in letters for e in list( e ) ): result.append( 'Yes' ) 
        else: result.append( 'No' )
    
    print ( '\n'.join( result ) )


func()