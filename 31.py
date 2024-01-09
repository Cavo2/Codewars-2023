# 31

l1 = { 'Hospital de Bellvitge': 100, 'Bellvitge': 108, 'Av. Carrilet': 204, 'Rbla. Just Oliveras': 173, 'Can Serra': 182, 'Florida': 130, 'Torrassa': 146, 'Santa Eulalia': 123, 'Mercat Nou': 197, 'Placa de Sants': 133, 'Hostafrancs': 164, 'Espanya': 149, 'Rocafort': 172, 'Urgell': 109, 'Universitat': 141, 'Catalunya': 190, 'Urquinaona': 166, 'Arc de Triomf': 217, 'Marina': 207, 'Glories': 280, 'Clot': 155, 'Navas': 216, 'La Sagrera': 186, 'Fabra i Puig': 210, 'Sant Andreu': 153, 'Torras i Bages': 138, 'Trinitat Vella': 146, 'Baro de Viver': 179, 'Santa Coloma': 104, 'Fondo': 144 }
l2 = { 'Parallel': 208, 'Sant Antoni': 163, 'Universitat': 141, 'Passeig de Gracia': 127, 'Tetuan': 217, 'Monumental': 152, 'Sagrada Familia': 114, 'Encants': 148, 'Clot': 155, 'Bac de Roda': 108, 'Sant Marti': 217, 'La Pau': 207, 'Verneda': 118, 'Artigues Sant Adria': 121, 'Sant Roc': 209, 'Gorg': 109, 'Pep Ventura': 212, 'Badalona Pompeu Fabra': 196 }
l3 = { 'Zona Universitaria': 165, 'Palau Reial': 216, 'Maria Cristina': 162, 'Les Corts': 164, 'Placa del Centre': 120, 'Sants Estacio': 204, 'Tarragona': 202, 'Espanya': 149, 'Poble Sec': 212, 'Parallel': 208, 'Drassanes': 176, 'Liceu': 176, 'Catalunya': 190, 'Passeig de Gracia': 127, 'Diagonal': 184, 'Fontana': 161, 'Lesseps': 197, 'Vallcarca': 203, 'Penitents': 106, "Vall d'Hebron": 150, 'Montbau': 195, 'Mundet': 201, 'Valldaura': 136, 'Canyelles': 109, 'Roquetes': 206, 'Trinitat Nova': 162 }
l4 = { 'La Pau': 207, 'Besos': 209, 'Besos de Mar': 126, 'El Maresme Forum': 208, 'Selva de Mar': 187, 'Poblenou': 134, 'Llacuna': 178, 'Bogatell': 176, 'Ciutadella Vila Olimpica': 154, 'Barceloneta': 103, 'Jaume I': 126, 'Urquinaona': 166, 'Passeig de Gracia': 127, 'Girona': 213, 'Verdaguer': 182, 'Joanic': 135, 'Alfons X': 220, 'Guinardo Hospital de Sant Pau': 171, 'Maragall': 206, 'Llucmajor': 213, 'Via Julia': 135, 'Trinitat Nova': 162 }
l5 = { 'Cornella Centre': 201, 'Gavarra': 201, 'Sant Ildefons': 108, 'Can Boixeres': 216, 'Can Vidalet': 190, 'Pubilla Cases': 186, 'Ernest Lluch': 158, 'Collblanc': 149, 'Badal': 165, 'Placa de Sants': 133, 'Sants Estacio': 204, 'Entenca': 112, 'Hospital Clinic': 101, 'Diagonal': 184, 'Verdaguer': 182, 'Sagrada Familia': 114, 'Sant Pau Dos de Maig': 215, "Camp de l'Arpa": 120, 'La Sagrera': 186, 'Congres': 120, 'Maragall': 206, 'Virrei Amat': 149, 'Vilapicina': 194, 'Horta': 175, 'El Carmel': 218, 'El Coll La Teixonera': 162, "Vall d'Hebron": 150 }

l1Transfers = [ ['Placa de Sants', 5], ['Espanya', 3], ['Universitat', 2], ['Catalunya', 3], ['Urquinaona', 4], ['Clot', 2], ['La Sagrera', 5] ]
l2Transfers = [ ['Parallel', 3], ['Universitat', 1], ['Passeig de Gracia', 3, 4], ['Sagrada Familia', 5], ['Clot', 1], ['La Pau', 4] ]
l3Transfers = [ ['Sants Estacio', 5], ['Espanya', 1], ['Parallel', 2], ['Catalunya', 1], ['Passeig de Gracia', 2, 4], ['Diagonal', 5], ["Vall d'Hebron", 5], ['Trinitat Nova', 4] ]
l4Transfers = [ ['La Pau', 2], ['Urquinaona', 1], ['Passeig de Gracia', 2, 3], ['Verdaguer', 5], ['Maragall', 5], ['Trinitat Nova', 3] ]
l5Transfers = [ ['Placa de Sants', 1], ['Sants Estacio', 3], ['Diagonal', 3], ['Verdaguer', 4], ['Sagrada Familia', 2], ['La Sagrera', 1], ['Maragall', 4], ["Vall d'Hebron", 3] ]

transfersRefs = { 1: [ l1, l1Transfers ], 2: [ l2, l2Transfers ], 3: [ l3, l3Transfers ], 4: [ l4, l4Transfers ], 5: [ l5, l5Transfers ] }

def toTransferStations ( station, ln ):
    result = []
    LN = transfersRefs[ ln ][0]
    transferLN = transfersRefs[ ln ][1]

    stationPos = list( LN.keys() ).index( station )

    for transferStation in transferLN:
        stationName = transferStation[0]
        transferStationPos = list( LN.keys() ).index( stationName )

        toTransferStationTime = 0
        route = []

        stationList = list( LN.items() )[ stationPos+1:transferStationPos+1 ] if transferStationPos > stationPos else list( LN.items() )[ stationPos-1:transferStationPos-1:-1 ]
        for name, time in stationList: 
            toTransferStationTime += time
            route.append( name )
        
        for i in transferStation[ 1: ]: result.append( [ stationName, route, toTransferStationTime, i ] ) # i is the station transfer lines

    return result


def toGoal ( station, ln, goal ):
    LN = transfersRefs[ ln ][0]

    stationPos = next ( ( pos for pos, e in enumerate( LN.keys() ) if e == station ), None )
    goalPos = next ( ( pos for pos, e in enumerate( LN.keys() ) if e == goal ), None )

    toGoalTime = 0
    route = []

    stationToGoalList = None
    if goalPos > stationPos : stationToGoalList = list ( LN.items() )[ stationPos+1:goalPos+1 ]
    elif goalPos == 0 and stationPos == 1: stationToGoalList = list ( LN.items() )[ goalPos::-1 ]
    else: stationToGoalList = list ( LN.items() )[ stationPos-1:goalPos-1:-1 ]

    for name, time in stationToGoalList:
        toGoalTime += time
        route.append( name )
    return [ route, toGoalTime ]



def func ():
    startStation = input ( 'Enter the starting station: ' )
    goalStation = input( 'Enter the goal station: ' )
    startStationN = [ pos for pos, value in enumerate( [ l1, l2, l3, l4, l5 ], start=1 ) for station in value if startStation == station ]
    goalStationN = [ pos for pos, value in enumerate( [ l1, l2, l3, l4, l5 ], start=1 ) for station in value if goalStation == station ]
    isSameLine = list ( set( startStationN ) & set( goalStationN ) )


    result = []
    def recurs ( station, ln, currentRoute, currentTime, recursNum ):
        if recursNum >= 4: return
        dataToEach = toTransferStations( station, ln )

        for e in dataToEach:
            if e[3] in goalStationN:
                toGoalData = toGoal( e[0], e[3], goalStation )
                route = currentRoute + e[1] + toGoalData[0]
                time = currentTime + e[2] + toGoalData[1] + 300
                result.append( [ [ startStation ] + route, time ] )
            else:
                route = currentRoute + e[1]
                time = currentTime + e[2] + 300
                recurs( e[0], e[3], route, time, recursNum+1 )

    [ recurs( startStation, LN, [], 0, 0 ) for LN in startStationN ]
    if len( isSameLine ):
        toGoalData = toGoal( startStation, isSameLine[0], goalStation )
        result.append( [ [ startStation ] + toGoalData[0], toGoalData[1] ] )

    result = sorted( result, key = lambda e: e[1] )
    result = result[0] # Get the fastest route
    result = [ result[1], ', '.join( result[0] ) ]
    print( f'Total time: { result[0] } seconds \nBest path from { startStation } to { goalStation }: \n{ result[1] }' )


func()


