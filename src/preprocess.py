import pandas as pd

def prepare_lap_data(session):
    laps = session.laps
    
    # Convert compound to numeric values
    compound_map = {'SOFT': 0, 'MEDIUM': 1, 'HARD': 2}
    laps['CompoundEncoded'] = laps['Compound'].map(compound_map)
    
    # Convert sector times to seconds
    laps['S1'] = laps['Sector1Time'].dt.total_seconds()
    laps['S2'] = laps['Sector2Time'].dt.total_seconds()
    laps['S3'] = laps['Sector3Time'].dt.total_seconds()
    
    # Convert LapTime to seconds
    laps['LapTime'] = laps['LapTime'].dt.total_seconds()
    
    # Drop rows with missing values
    laps = laps.dropna(subset=['S1', 'S2', 'S3', 'TyreLife', 'CompoundEncoded', 'LapTime'])
    
    # Select required columns
    return laps[["S1", "S2", "S3", "TyreLife", "CompoundEncoded", "LapTime"]]