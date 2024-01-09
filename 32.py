import copy 

# 32


def increaseLifeTime ( matrix ):
    newMatrix = copy.deepcopy( matrix )
    for row, rowEl in enumerate( matrix ):
        for col, colEl in enumerate( rowEl ):
            if type( colEl[1] ) == int: newMatrix[ row ][ col ][1] += 1
    return newMatrix

def replication ( matrix ):
    newMatrix = copy.deepcopy( matrix )
    for row, rowEl in enumerate( matrix ):
        for col, colEl in enumerate( rowEl ):
            elName = colEl[0]
            if not elName.isalpha(): continue
            elLifetime = speciesData[ elName ][0][1]
            if colEl[1] == 0 or colEl[1] == elLifetime: continue

            elGrowthPattern = speciesData[ elName ][1] # Get the growth pattern relative to the center
            growthPatternWidth = len( elGrowthPattern[0] )
            growthPatternHeight = len( elGrowthPattern )
            growthPatternCenter = [ (growthPatternWidth-1)/2+1, (growthPatternHeight-1)/2+1 ] # Get the center
            growthPos = [ [ row, col ] for row, rowValue in enumerate( elGrowthPattern, start=1 ) for col, colValue in enumerate( rowValue, start=1 ) if colValue == 1 ] # Get the positions where there is 1
            posRelativeToCenter = [ [ int( e[0] - growthPatternCenter[1] ), int( e[1] - growthPatternCenter[0] ) ] for e in growthPos ] # The row is associated to the height and the col to the width


            for e in posRelativeToCenter: # With the relative pattern, change the items of the matrix according to the empty spaces and items resilience
                maxRow = list( range( 0, len( matrix ) ) )
                maxCol = list( range( 0, len( matrix[0] ) ) )
                if not row + e[0] in maxRow or not col + e[1] in maxCol: continue

                newPos = newMatrix[ row + e[0] ][ col + e[1] ]
                if newPos[0] == '_' or newPos[0] == elName: continue
                elif newPos[0] == '.': newMatrix[ row + e[0] ][ col + e[1] ] = [ elName, 0 ]
                else: 
                    newPosItemName = newPos[0]
                    itemResilience = speciesData[ newPosItemName ][0][0]
                    thisItemResilience = speciesData[ elName ][0][0]
                    if itemResilience > thisItemResilience: continue
                    else: newMatrix[ row + e[0] ][ col + e[1] ] = [ elName, 0 ]
    return newMatrix


def deleteOlds ( matrix ):
    newMatrix = copy.deepcopy( matrix )
    for row, rowEl in enumerate( matrix ):
        for col, colEl in enumerate( rowEl ):
            elName = colEl[0]
            if not elName.isalpha(): continue
            
            thisItemMaxTime = int( speciesData[ elName ][0][1] )
            thisItemTime = int( colEl[ 1 ] )
            if thisItemTime < thisItemMaxTime: continue
            else: newMatrix[ row ][ col ] = [ '.', '.' ]
    return newMatrix




speciesData = {}

def func ():
    species = int ( input( 'Enter the amount of species: ' ) )
    for i in range( 0, species ):
        specieName = input( 'Enter specie name: ' )
        resilenceAndTime = list( map( int, input ( 'Enter resilence and lifetime: ' ).split() ) )

        growthSize = list( map( int, input ( 'Enter the growthSize: ' ).split() ) )
        growthMatrix = []
        for i in range( 0, growthSize[0] ):
            growthPatterLine = list( map( int, list( input( 'Enter growth patter line: ' ) ) ) )
            growthMatrix.append( growthPatterLine )
        speciesData[ specieName ] = [ resilenceAndTime, growthMatrix ]
        
    experimentMatrix = []
    experimentSize = list( map( int, input( 'Enter the experiment size: ' ).split() ) )
    for i in range( 0, experimentSize[0] ): 
        experimentMatrixLine = list( input( 'Enter experiment grid line: ' ) )
        experimentMatrixLine = list( map ( lambda e: [ e, 0 ] if e.isalpha() else [ e, e ], experimentMatrixLine ) )
        experimentMatrix.append( experimentMatrixLine )


    simulationDays = int( input( 'Enter simulation days: ' ) )

    result = [ experimentMatrix ]
    currentMatrix = experimentMatrix
    for i in range( 0, simulationDays ):
        increasedTime = increaseLifeTime ( currentMatrix )
        replicate = replication( increasedTime )
        deleteOlders = deleteOlds( replicate )
        result.append( deleteOlders )
        currentMatrix = deleteOlders
    
    daysResults = []
    for day, dayValue in enumerate( result ):
        aliveAndAgeResults = []
        for row in dayValue:
            aliveResultRow, ageResultRow = '', ''
            for col in row:
                aliveResultRow += str( col[0] )
                ageResultRow += str( col[1] )
            aliveAndAgeResults.append( aliveResultRow + '   ' + ageResultRow )
        daysResults.append( f'Mushrooms at day { day }\n' + '\n'.join( aliveAndAgeResults ) )
    print( '\n\n'.join( daysResults ) )


func ()

