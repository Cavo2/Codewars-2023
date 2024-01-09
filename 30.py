# 30

def func ():
    ridersInput, resultsInput = [], []
    while True:
        inputValue = input ()
        if len( ridersInput ) == 0 or ridersInput[ -1 ] != ['#']: ridersInput.append( inputValue.split( ' ' ) )
        elif inputValue != '#': resultsInput.append( inputValue.replace( '|', '_' ).split( '_' ) )
        else: break

    riders, teams, brands = [], [], []
    for e in resultsInput: 
        extraPointRider = e[ -1 ] # Get the last element, it is the extra point player
        extraPoint = list( filter( lambda team: extraPointRider in team, ridersInput ) )[0] # Get it's teams
    
        riderInArry = next( ( pos for pos, e in enumerate( riders ) if extraPoint[0] in e ), None ) # Add the point for the rider
        if riderInArry is not None : riders[ riderInArry ][1] += 1 
        else: riders.append( [ extraPoint[0], 1, 0 ] ) 

        teamInArry = next( ( pos for pos, e in enumerate( teams ) if extraPoint[1] in e ), None ) # Add the point for it's team
        if teamInArry is not None: teams[ teamInArry ][1] += 1  
        else: teams.append( [ extraPoint[1], 1, 0 ] ) 

        brandInArry = next( ( pos for pos, e in enumerate( brands ) if extraPoint[2] in e ), None ) # Add the point for it's brand
        if brandInArry is not None: brands[ brandInArry ][1] += 1  
        else: brands.append( [ extraPoint[2], 1, 0 ] ) 

        pointsRefs = { 0: 10, 1: 8, 2: 6, 3: 4, 4: 3, 5: 2, 6: 1 }

        for pos, finalist in enumerate( e[ :-1 ] ):
            if pos > 6: break

            points = pointsRefs[ pos ]

            riderTeam = list ( filter ( lambda team: finalist in team, ridersInput ) )[0]

            riderInArry = next( ( pos for pos, e in enumerate( riders ) if riderTeam[0] in e ), None ) # Add the point for the rider
            if riderInArry is not None: riders[ riderInArry ][1] += points  
            elif pos == 0: riders.append( [ riderTeam[0], points, 1 ] ) 
            else: riders.append( [ riderTeam[0], points, 0 ] ) 
            if pos == 0 and riderInArry is not None: riders[ riderInArry ][2] += 1

            teamInArry = next( ( pos for pos, e in enumerate( teams ) if riderTeam[1] in e ), None ) # Add the point for it's team
            if teamInArry is not None: teams[ teamInArry ][1] += points  
            elif pos == 0: teams.append( [ riderTeam[1], points, 1 ] ) 
            else: teams.append( [ riderTeam[1], points, 0 ] ) 
            if pos == 0 and teamInArry is not None: teams[ teamInArry ][2] += 1

            brandInArry = next( ( pos for pos, e in enumerate( brands ) if riderTeam[2] in e ), None ) # Add the point for it's brand
            if brandInArry is not None: brands[ brandInArry ][1] += points  
            elif pos == 0: brands.append( [ riderTeam[2], points, 1 ] ) 
            else: brands.append( [ riderTeam[2], points, 0 ] ) 
            if pos == 0 and brandInArry is not None: brands[ brandInArry ][2] += 1
    
    riders = sorted( riders, key = lambda e: ( e[1], e[2] ), reverse = True )
    teams = sorted( teams, key = lambda e: ( e[1], e[2] ), reverse = True )
    brands = sorted( brands, key = lambda e: ( e[1], e[2] ), reverse = True )

    result = []
    titleRefs = { 0: 'Riders', 1: 'Teams', 2: 'Brands' }
    for pos, e in enumerate( [ riders, teams, brands ] ):
        result.append( f'{ titleRefs[ pos ] } Classification:' )
        for i in range( 0, 3 ):
            result.append( f'{ i } - { e[i][0] } - { e[i][1] } pts - { e[i][2] } wins' )
    print( '\n'.join( result ) )


func()
