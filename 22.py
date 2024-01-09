import math

# 22

def getWeekDay ( day, month, year ):
    if month < 3: 
        month += 12
        year -= 1

    century = int( year / 100 )
    yearOfCentury = year % 100

    result = math.floor( 2.6*month - 5.39 ) + math.floor( yearOfCentury/4 ) + math.floor( century/4 )
    result = result + day + yearOfCentury - ( 2*century )
    result = result % 7 
    return result 

def func ():
    result = []
    yearInput = input( 'Year: ' )
    for i in range( 1, 13 ):
        weekDay = getWeekDay( 13, i, int( yearInput ) )
        if weekDay == 2: result.append( f'Martes y Trece will occur on 13/{i}/{yearInput}' )
    for e in result:
        print( e )

func() 

