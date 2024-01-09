def func ():
    arry = []
    for i in range( 0, 4 ):
        inputNumber = int( input( 'Enter a number: ' ) )
        arry.append( inputNumber )
    
    totalPoints = arry[0]*1 + arry[1]*2 + arry[2]*3
    totalThrows = arry[0]+arry[1]+arry[2]
    effectiveness = int( totalThrows * 100 / arry[3] )
    result =  f'Total points: { totalPoints }. Effectiveness percentage: { effectiveness }%'
    
    print( result )

func()
