from functools import reduce

# 23

def getAroundCoordenates ( row, col ):
    return [ [ row-1, col-1 ], [ row-1, col ], [ row-1, col+1 ], [ row, col-1 ], [ row, col+1 ], [ row+1, col-1 ], [ row+1, col ], [ row+1, col+1 ] ]

def func ():
    areaLevel = input( 'Enter level: ' )
    areaLevelRefs = { 'Easy': 3, 'Medium': 6, 'Hard': 9 }
    areaLevel = areaLevelRefs[ areaLevel ]
    numberOfMines = int( input( 'Enter number of mines: ' ) )
    coordenatesArray = []
    result = ''

    for i in range( numberOfMines ): # Store coordenates
        coordenate = input( 'Enter coordenate: ' )
        coordenate = list( map( lambda e: int( e ), coordenate.strip().split( ' ' ) ) )
        coordenatesArray.append( coordenate )

    for row in range( 1, areaLevel+1 ):
        for col in range( 1, areaLevel+1 ): 
            if [ row, col ] in coordenatesArray: 
                result += '# '
                continue
            aroundCoords = getAroundCoordenates( row, col )
            levelOfDanger = reduce( lambda acc, e: acc+1 if e in coordenatesArray else acc, aroundCoords, 0 )
            result += f'{levelOfDanger} '
        result += '\n'

    print( result )


func()
