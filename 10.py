from functools import reduce

def func ():
    inputNumbers = []
    while True: 
        inputNumber = input( 'Enter number or #: ' )
        if inputNumber == '#': break
        inputNumbers.append( int( inputNumber ) )

    result = []
    for pos, e in enumerate( inputNumbers ):
        filteredArray = list( map( lambda e: e[1], filter( lambda e: pos != e[0], enumerate( inputNumbers ) ) ) )
        sumResult = reduce( ( lambda acc, e: acc + e ), filteredArray, 0 )
        productResult = reduce( ( lambda acc, e: acc * e ), filteredArray, 1 )
        result.append( [ sumResult, productResult ] )
    
    sumResult = reduce( ( lambda acc, e: acc + str( e[0] ) + ' ' ), result, '' )
    productResult = reduce( ( lambda acc, e: acc + str( e[1] ) + ' ' ), result, '' )
    print( sumResult + '\n' + productResult )

func ()