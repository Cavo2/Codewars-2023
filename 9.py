
def func ():
    frequency = int( input( 'Enter frequency: ' ) )
    sound = int( input( 'Enter speed of the sound waves: ' ) )
    observer = int( input( 'Enter velocity of the observer: ' ) ) * 1000 / 3600
    object = int( input( 'Enter velocity of the noisy object: ' ) ) * 1000 / 3600

    result = frequency * ( sound + observer ) / ( sound + object )
    print( f'{ round( result, 2 ) } Hz' )


func()
