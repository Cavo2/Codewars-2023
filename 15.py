# 15

def manageInput ( input ):
    splitedInput = input.split( ' ' )
    valuesWithoutName = ' '.join( splitedInput[ 1: ] )
    firstValues = valuesWithoutName.split( '#' )[0].strip()
    secondValues = valuesWithoutName.split( '#' )[1].strip()
    firstSplitedValues = firstValues.split( ' ' )
    secondSplitedValues = secondValues.split( ' ' )[ ::-1 ]
    condition = all ( firstSplitedValues[i] == secondSplitedValues[i] for i in range( len(firstSplitedValues)-1 ) )
    text = splitedInput[0] + ' has same number of steps for both faces' if condition else splitedInput[0] + ' has NOT same number of steps for both faces'
    print( text )
    

def func ():
    amount = int( input( 'Enter amount: ' ) )
    arry = []
    for i in range( amount ): # Get the values
        newInput = input()
        arry.append( newInput )
    [ manageInput( e ) for e in arry ]


func()