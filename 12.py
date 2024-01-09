def func ():
    wordToGuess = input( 'Enter the word to guess: ' )
    letters = list( input( 'Enter the letters: ' ) )
    lives = 7

    finalWord = [ '_' ] * len( wordToGuess )
    for letter in letters:
        if lives == 0: break
        if letter in wordToGuess:
            lettersPos = list( map( lambda e: e[0], filter ( ( lambda e: e[1] == letter ), enumerate( wordToGuess ) ) ) )
            for pos in lettersPos: finalWord[ pos ] = wordToGuess[ pos ]
        else: lives -= 1
    
    message = 0
    if lives == 0: message = 'Player loses.'
    elif lives > 0 and not '_' in finalWord: message = 'Player wins!'
    else: message = 'Word not completed and player is still alive.'

    print( f'{ "_"*len( wordToGuess ) } \n{ "".join( finalWord ) } \n{ message } \nLives: { lives }' )

func()