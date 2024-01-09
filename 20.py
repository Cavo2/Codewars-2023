# 20

def getRow ( n ):
    result = n / 9
    if n % 9 != 0: result += 1
    return int( result )

def getCol ( n ):
    result = n % 9
    if result == 0: result = 9
    return int( result )

def getSector ( n ):
    row = getRow ( n )
    col = getCol ( n )

    if row < 4: row = [ 1, 2, 3 ]
    elif row > 3 and row < 7: row = [ 4, 5, 6 ]
    else: row = [ 7, 8, 9 ]
    
    if col < 4: return row[0]
    elif col > 6: return row[2]
    else: return row[1]

def func ():
    sudokuInput = input()
    counter = 0
    numArry = list( map ( lambda e: int( e ), sudokuInput.split( ' ' ) ) )
    for p, e in enumerate( numArry, start = 1 ):
        values = [ getRow( p ), getCol( p ), getSector( p ) ]
        if e in values: counter += 1
    print( f'Number of friends = { counter }' )

func()

