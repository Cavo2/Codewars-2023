# 7

def func ():
    gender = input( 'Enter gender: ' )
    redBloodCells = float( input( 'Enter red blood cells: ' ) )
    whiteBloodCells = float( input( 'Enter white blood cells: ' ) )
    platelets = float( input( 'Enter platelets: ' ) )
    hemoglobin = float( input( 'Enter hemoglobin: ' ) )
    hematocrit = float( input( 'Enter hematocrit: ' ) )


    whiteBloodCells = 'NORMAL' if whiteBloodCells > 4500 and whiteBloodCells < 11000 else 'VISIT THE DOCTOR'
    platelets = 'NORMAL' if platelets > 150000 and platelets < 400000 else 'VISIT THE DOCTOR'
    if gender == 'Male':
        redBloodCells = 'NORMAL' if redBloodCells > 4.3 and redBloodCells < 5.9 else 'VISIT THE DOCTOR'
        hemoglobin = 'NORMAL' if hemoglobin > 13.5 and hemoglobin < 17.5 else 'VISIT THE DOCTOR'
        hematocrit = 'NORMAL' if hematocrit > 41 and hematocrit < 53 else 'VISIT THE DOCTOR'
    elif gender == 'Female': 
        redBloodCells = 'NORMAL' if redBloodCells > 3.5 and redBloodCells < 5.5 else 'VISIT THE DOCTOR'
        hemoglobin = 'NORMAL' if hemoglobin > 12.0 and hemoglobin < 16.0 else 'VISIT THE DOCTOR'
        hematocrit = 'NORMAL' if hematocrit > 36 and hematocrit < 46 else 'VISIT THE DOCTOR'
    result = f'Red blood cells: { redBloodCells } \nWhite blood cells: { whiteBloodCells } \nPlatelets: { platelets } \nHemoglobin: { hemoglobin } \nHematorcrit: { hematocrit }'
    
    print( result )
        
func()