import math

# 19

meters = input( 'Enter meter: ' )
degrees = input( 'Enter degree: ' )

def gradesToRadians ( degree ):
    return math.pi / 180 * degree

def func ( meters, degree ):
    radians = gradesToRadians ( degree )
    minDistance = meters - 3 + ( 0.0427/2 )
    maxDistance = meters + 3 - ( 0.0427/2 )
    minTime = math.sqrt( 2 * minDistance * math.sin( radians ) / ( 9.8 * math.cos( radians ) ) )
    maxTime = math.sqrt( 2 * maxDistance * math.sin( radians ) / ( 9.8 * math.cos( radians ) ) )
    minSpeed = minDistance / ( math.cos( radians ) * minTime )
    maxSpeed = maxDistance / ( math.cos( radians ) * maxTime )
    print( f'The maximum speed is: { round( maxSpeed, 2 ) } m/s. \nThe minimum speed is: { round( minSpeed, 2 ) } m/s.' )
    

func( int( meters ), int( degrees ) )

