# 33

def draw ( drawingSpace, xyz ):
    [ x, y, z ] = xyz
    around = [ [ x-1, y-1, '+' ], [ x, y-1, '-' ], [ x+1, y-1, '+' ], [ x-1, y, '|' ], [ x+1, y, '|' ], [ x-1, y+1, '+' ], [ x, y+1, '-' ], [ x+1, y+1, '+' ] ]
    for e in around:
        rowPos = e[0] + 2 # Plus two to place it in the center
        colPos = e[1]
        if drawingSpace[ colPos ][ rowPos ] == ' ': drawingSpace[ colPos ][ rowPos ] = [ e[2], z ]
        elif drawingSpace[ colPos ][ rowPos ][1] == z and drawingSpace[ colPos ][ rowPos ][0] != '+': drawingSpace[ colPos ][ rowPos ] = ' '

    drawingSpace = [ list( map( lambda col: ' ' if ( # Deletes symbols that are not a edge
        row > 0 and row < 24 and
        col[0] > 0 and col[0] < 24 and 
        drawingSpace[ row - 1 ][ col[0] ] == ' ' and 
        drawingSpace[ row + 1 ][ col[0] ] == ' ' and 
        drawingSpace[ row ][ col[0] - 1 ] == ' ' and 
        drawingSpace[ row ][ col[0] + 1 ] == ' '
    ) else col[1], enumerate( rowEl ) ) ) for row, rowEl in enumerate( drawingSpace ) ]
    
    return drawingSpace



def func ():
    viewInput = input( 'Enter view input: ' )
    numberOfBoxes = int( input ( 'Enter the number of boxes: ' ) )
    coords = []
    for i in range( 0, numberOfBoxes ):
        boxCoords = list( map ( int, input( 'Enter box coordinates: ' ).split() ) )
        coords.append( boxCoords )
    projectionRefs = { 'FRONT': [ 0, 1, 2 ], 'REAR': [ 0, 1, 2 ], 'TOP': [ 0, 2, 1 ], 'BOTTOM': [ 0, 2, 1 ], 'LEFT': [ 2, 1, 0 ], 'RIGHT': [ 2, 1, 0 ] } # First two values are the projection axes and third value is the view axis
    projectionAxes = projectionRefs[ viewInput ]

    drawingSpace = []
    for i in range( 0, 25 ):
        if i == 0 or i == 24: drawingSpace.append( list( '#'*25 ) )
        else: drawingSpace.append( list ( '#' + ' '*23 + '#' ) )

    for xyz in coords:
        horizontalAxe = xyz[ projectionAxes[0] ] * 2 # Multiply two to convert it to 2D symbols grid position
        verticalAxe = xyz[ projectionAxes[1] ] * 2
        viewAxe = xyz[ projectionAxes[2] ] * 2 # This is the axe where you look
        if viewInput == 'FRONT': verticalAxe = 22 - verticalAxe # This is for invert the axe
        if viewInput == 'BOTOM': verticalAxe = 22 - verticalAxe
        if viewInput == 'RIGHT': verticalAxe = 22 - verticalAxe
        if viewInput == 'LEFT': 
            verticalAxe = 22 - verticalAxe
            horizontalAxe = 22 - horizontalAxe
        if viewInput == 'REAR': 
            verticalAxe = 22 - verticalAxe
            horizontalAxe = 22 - horizontalAxe

        drawingSpace = draw( drawingSpace, [ horizontalAxe, verticalAxe, viewAxe ] )

    result = [ ''.join( list ( map ( lambda e: e if e == ' ' or e == '#' else e[0] , row ) ) ) for row in drawingSpace ]

    firstSpaces, lastSpaces, content, toogleSpaces = [], [], [], False # This is for toogle top and bottom spaces
    if viewInput == 'TOP': 
        for e in result[ 1:-1 ]:
            if '#                       #' == e and toogleSpaces == False: 
                firstSpaces.append( e )
            elif '#                       #' == e and toogleSpaces == True: 
                lastSpaces.append( e )
            elif toogleSpaces == False: 
                content.append( e )
                toogleSpaces = True
            else: 
                content.append( e )
                continue 
        result = [ result[0] ] + lastSpaces + content + firstSpaces + [ result[0] ]
    result = '\n'.join( result )

    print( result )

    
func ()
