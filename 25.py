import math

# 25

def isPrime ( n ):
    n = int( n )
    if n < 2: return False
    for i in range( 2, int( math.sqrt( n ) ) + 1 ):
        if n % i == 0: return False
    return True

def primePos ( n ):
    n = int( n )
    pos = 0
    for i in range( 2, n+1 ):
        if isPrime( i ): pos += 1
    return str( pos )

def func ():
    numInput = input( 'Enter number: ' )
    reversedNum = numInput[ ::-1 ]
    [ numIsPrime, reversedIsPrime, numPrimePos, reversedPrimePos ] = [ isPrime( numInput ), isPrime( reversedNum ), primePos( numInput ), primePos( reversedNum ) ]
    if not numIsPrime or not reversedIsPrime: print( 'Number N is not related to Sheldon prime' )
    elif numPrimePos == reversedPrimePos[ ::-1 ]: print( f'Number {numInput} is a Sheldon prime!' )
    elif all ( n in reversedPrimePos for n in numPrimePos ) and len( numPrimePos ) == len( reversedPrimePos ): 
        print( f'Number {numInput} is a Sheldon prime relative' )
    elif isPrime ( numPrimePos ) and isPrime ( reversedPrimePos ): print ( f'Number {numInput} is a close friend of Sheldon prime' )
    else: print( f'Number {numInput} is a friend of Sheldon prime' )

func()

