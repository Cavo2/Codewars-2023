from functools import reduce

# 29

pizzas = [ 'Rustica', 'Romana', 'Prosciutto e funghi', 'Funghi', 'Pesto Genovese', 'Bianca', 'Carbonara', 'Sicilian', 'California', 'Hawaiian', 'Pinsa Romana', 'Caprese', 'Vegetariana', 'Quattro formaggi', 'Diavola', 'Pepperoni', 'Quattro stagioni', 'Calzone', 'Frutti di mare', 'Margherita', 'Prosciutto', 'Napoletana' ]

def func ():
    pizzasOrdered = []
    while True:
        pizzaInput = input( 'Enter pizza name: ' )
        if pizzaInput == '#': break
        pizzasOrdered.append( pizzaInput )

    listedPizzas = []
    for e in pizzasOrdered:
        if not e in pizzas: # The pizza name is wrong
            listedPizzas.append( [ e, -1 ] )
            continue
        elif e in [ e[0] for e in listedPizzas ]: # The pizza is already in the array
            index = [ p for p, value in enumerate( listedPizzas ) if value[0] == e ][0]
            currentAmount = listedPizzas[ index ][ 1 ]
            listedPizzas[ index ][ 1 ] = currentAmount + 1
        else: listedPizzas.append( [ e, 1 ] ) # A normal pizza that is not added yet
    
    sortedPizzas = sorted( listedPizzas, key = lambda e: ( -e[1], e[0] ) )

    validPizzas = list( filter( lambda e: e[1] > 0, sortedPizzas ) )
    invalidPizzas = list( filter( lambda e: e[1] == -1, sortedPizzas ) )

    validRequests = reduce( lambda acc, e: acc + e[1], validPizzas, 0 )
    result = [ f'Received valid pizza requests: { validRequests }' ]
    [ result.append( f'{ e[0] } { e[1] if e[1] != 1 else "" }' ) for e in validPizzas ]
    result.append( '---' )
    result.append( f'Invalid requests: { len( invalidPizzas ) }' ) 
    [ result.append( f'{ e[0] }' ) for e in invalidPizzas ]

    print( '\n'.join( result ) )

    
func ()