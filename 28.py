from functools import reduce

# 28

communities_flags = {
    'Andalucia': [ [0, 102, 51], [255, 255, 255], [255, 228, 77] ],
    'Aragon': [ [252, 221, 9], [218, 18, 26], [15, 71, 175] ],
    'Canarias': [ [255, 255, 255], [7, 104, 169], [255, 204, 0] ],
    'Cantabria': [ [255, 255, 255], [237, 28, 36], [0, 113, 188] ],
    'Castilla-La Mancha': [ [162, 28, 28], [255, 204, 0], [0, 0, 0] ],
    'Castilla y Leon': [ [116, 44, 100], [255, 255, 255], [252, 221, 9] ],
    'Catalunya': [ [252, 221, 9], [218, 18, 26] ],
    'Comunidad de Madrid': [ [198, 11, 30], [255, 255, 255] ],
    'Comunidad Foral de Navarra': [ [237, 45, 29], [227, 228, 229], [234, 193, 2] ],
    'Comunidad Valenciana': [ [0, 114, 188], [218, 18, 26], [252, 221, 9] ],
    'Extremadura': [ [100, 0, 67], [255, 255, 255], [0, 0, 0] ],
    'Galicia': [ [0, 153, 204], [255, 255, 255], [0, 91, 191] ],
    'Islas Baleares': [ [252, 221, 9], [218, 18, 26], [255, 255, 255] ],
    'La Rioja': [ [181, 41, 33], [255, 255, 255], [0, 0, 0] ],
    'Pais Vasco': [ [213, 43, 30], [255, 255, 255], [0, 155, 72] ],
    'Principado de Asturias': [ [0, 102, 255], [247, 212, 23] ],
    'Region de Murcia': [ [156, 31, 45], [252, 183, 20] ]
}

def absoluteDifference ( a, b ):
    return abs( a[0] -  b[0] ) + abs( a[1] -  b[1] ) + abs( a[2] -  b[2] )

def func ():
    rgbArry = []
    while True: # Get the inputs
        if len( rgbArry ) == 3: break

        rgbInput = input( 'Enter Value or #: ' )
        if rgbInput == '#': break
        else: rgbArry.append( [ int( e ) for e in rgbInput.split( ' ' ) ] )
    

    sortedCommunities = [ [ 'x', 999 ] ]
    for key, value in communities_flags.items(): 
        if len( rgbArry ) > len( value ): continue # if the amount of colors of the input is greather than the flag amount, continue

        colorDifference = reduce( lambda acc, e: acc + e, [ absoluteDifference( e, value[p] ) for p, e in enumerate( rgbArry ) ], 0 ) # Get the color difference between the flag and the input

        for p, e in enumerate( sortedCommunities ): # Insert the value to it's appropriate position
            if colorDifference <= e[1]: 
                sortedCommunities.insert( p, [ key, colorDifference ] )
                break
            else: continue

    # Put it in the right format
    result = [] 
    firstCommunities = sorted( list( filter( lambda e: e[1] == sortedCommunities[0][1], sortedCommunities ) ), key = lambda e: tuple( ord( char ) for char in e[0] ) ) # Sort alphabetically
    sortedCommunities = list( filter( lambda e: e[1] != sortedCommunities[0][1], sortedCommunities ) )
    secondCommunities = list( filter( lambda e: e[1] == sortedCommunities[0][1], sortedCommunities ) )
    for p, e in enumerate( [ firstCommunities, secondCommunities ] ):
        posRefs = { 0: '1st', 1: '2nd' }
        if len( e ) > 1: 
            [ result.append( f'{ posRefs[p] } community flags: { community[0] } with difference: { community[1] }' ) for community in e ]
        else: result.append( f'{ posRefs[p] } community flag: { e[0][0] } with difference: { e[0][1] }' )
    
    print( '\n'.join( result ) )


func()
