import math 

# 26


def intersect ( a, b ):
    a = [ int( e ) for e in a ] # Convert arry elements in int
    b = [ int( e ) for e in b ]
    d = math.sqrt( ( a[0] - b[0] )*( a[0] - b[0] ) + ( a[1] - b[1] )*( a[1] - b[1] ) ) # Get the distance, this is just the formula
    if d <= ( a[2] - b[2] ) or d <= ( b[2] - a[2] ) or d < ( a[2] + b[2] ) or d == ( a[2] + b[2] ): return True # Return true if it colides
    else: return False


def func ():
    detonator = input ( 'Enter detonator: ' ).split( ' ' )
    particlesNum = int( input( 'Enter particles num: ' ) )
    particles = []
    for i in range( 0, particlesNum ):
        particle = input ()
        particles.append ( particle.split( ' ' ) )

    def recurs ( reaction ):
        for i, e in enumerate( particles ):
            if e[ -1 ] == True: continue
            if intersect( reaction, e[ 0:3 ] ): 
                particles[i].append( True )
                recurs( [ e[0], e[1], e[3] ] ) # This is the colided particle reaction radius
    recurs ( detonator )

    result = []
    for e in particles:
        result.append( f'({ e[0] }, { e[1] }) { "HIT" if e[ -1 ] == True else "NOT HIT" }' )
    print( '\n'.join( result ) )


func()
