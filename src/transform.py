from typing import Tuple

import numpy as np

import pandas as pd

def station_temps_dataframes(database: dict, months: pd.DataFrame, i: int) -> Tuple[pd.DataFrame,pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:

# Taking the station name and location.  
    station = database['location'].iloc[i,1:]

# Defining a dataframe with the extremes temperatures of the year. 
    cols = pd.MultiIndex.from_product([['Extremes'],['Max.','Day','Min.','Day']])
    extr_T = pd.DataFrame() 

    aux_df = pd.DataFrame([database['max_T'].iloc[i,2:], database['day_Tmax'].iloc[i,2:], database['min_T'].iloc[i,2:], 
                           database['day_Tmin'].iloc[i,2:]]).T.reset_index(drop=True)

# Here, the extremes temperatures of each month are highlighted with the date of the event. 
    m = aux_df.iloc[:,0].idxmax()
    extr_T['Max.'] = aux_df.iloc[:,0].tolist() + [aux_df.iloc[:,0].max()]
    extr_T['Day'] = list(aux_df.iloc[:,1].astype(int).astype(str)) + [months.Month[m]]

    m = aux_df.iloc[:,2].idxmin()
    extr_T['Min.'] = aux_df.iloc[:,2].tolist() + [aux_df.iloc[:,2].min()]
    extr_T['Day_x'] = list(aux_df.iloc[:,3].astype(int).astype(str)) + [months.Month[m]]

    extr_T.columns = cols

# Defining a dataframe with the average temperatures of each month.  
    cols = pd.MultiIndex.from_product([['Means'],['Max.','Min.','Avg.']])
    avg_T = pd.DataFrame()

# The last row of each column contains the mean of the column.
    avg_T['Max.'] = np.round(database['avg_Tmax'].iloc[i,2:].tolist() + [database['avg_Tmax'].iloc[i,2:].mean()],1)
    avg_T['Min.'] = np.round(database['avg_Tmin'].iloc[i,2:].tolist() + [database['avg_Tmin'].iloc[i,2:].mean()],1)
    avg_T['Avg.'] = np.round(database['avg_T'].iloc[i,2:].tolist() + [database['avg_T'].iloc[i,2:].mean()],1)

    avg_T.columns = cols

# Defining a dataframe with categorical temperatures data through the year. 
    cate_T = pd.DataFrame()

# The last row of each column show the total of events in the year.
    cate_T['T \u2264 0'] = database['t_0'].iloc[i,2:].tolist() + [database['t_0'].iloc[i,2:].sum()]
    cate_T['0 \u2264 T \u2264 5'] = database['t_0_5'].iloc[i,2:].tolist() + [database['t_0_5'].iloc[i,2:].sum()]
    cate_T['35 \u2264 T \u2264 40'] = database['t_35_40'].iloc[i,2:].tolist() + [database['t_35_40'].iloc[i,2:].sum()]
    cate_T['T \u2265 40'] = database['t_40'].iloc[i,2:].tolist() + [database['t_40'].iloc[i,2:].sum()]

# Storing the dew point data of the current station into an idividual dataframe.
    lst = np.round(database['dew_T'].iloc[i,2:].tolist() + [database['dew_T'].iloc[i,2:].mean()],1)
    dew_T = pd.DataFrame(lst, columns=['    Avg. Relative\n Moisture.'])

    return extr_T,avg_T,cate_T,dew_T,station
    
def station_vars_dataframes(months: pd.DataFrame, database: dict, i: int) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:    
# Taking the station name and location. 
    station = database['location'].iloc[i,1:]

# Initializing a dataframe for heliophany data.
    cols = pd.MultiIndex.from_product([['Heliophany'],['Mean','Total']])
    heliophany = pd.DataFrame(columns=cols)

# Transforming dataframe columns into lists.
    aux_1 = database['avg_helio'].iloc[i,2:].tolist()
    aux_2 = database['total_helio'].iloc[i,2:].tolist()
# Last two rows contain the total and the average heliophany meassurements of the year
    heliophany[('Heliophany', 'Mean')] = np.round(aux_1 + [np.mean(aux_1)],1)
    heliophany[('Heliophany', 'Total')]= np.round(aux_2 + [database['avg_helio'].iloc[i,2:].sum()],1)
# Rounding the dataframe to one decimal value.    
    heliophany.round(1)

# Initializing a dataframe for the atm. preassure data.
    cols = pd.MultiIndex.from_product([['Avg. Atm. Pres.'],['Sea Level','Station Level']])
    pres = pd.DataFrame()

# Torning dataframe columns into lists.
    aux_1 = database['qnh'].iloc[i,2:].tolist()
    aux_2 = database['qne'].iloc[i,2:].tolist()
# Last row of the dataframe refers to the average values of atm. preassure of each kind.
    pres['Sea Level'],pres['Station Level'] = np.round(aux_1 + [np.mean(aux_1)],1), np.round(aux_2 + [np.mean(aux_2)],1)

    pres.columns = cols

# Initializing a dataframe with precipitation data.
    cols = pd.MultiIndex.from_product([['Rainfall'],['Máx. in 24hs','Day','Total', 'Days with Rain']])
    rain = pd.DataFrame()

# Storing each needed data into one dataframe.
    aux_df = pd.DataFrame([database['max_rainfall_24'].iloc[i,2:], database['max_rainfall_24_day'].iloc[i,2:], database['rainfall'].iloc[i,2:], database['rainfall_days'].iloc[i,2:]]).T.reset_index(drop=True)

# Setting the precipitation dataframe and putting in the last row summary information:
# max. precipitation in the year,
# month where this max. value took place,
# total amount of rain in the year,
# and total days with precipitation.
    m=aux_df.iloc[:,0].idxmax()
    rain['Máx. in 24hs'] = aux_df.iloc[:,0].tolist() + [aux_df.iloc[:,0].max()] 
    rain['Day'] = list(aux_df.iloc[:,1].astype(int).astype(str)) + [months.Month[m]]
    rain['Total'] = np.round(aux_df.iloc[:,2].tolist() + [aux_df.iloc[:,2].sum()],1)
    lst = list(aux_df.iloc[:,3].astype(int).astype(str))
    rain['Days with Rain'] = lst + [str(int(aux_df.iloc[:,3].sum()))]
    
    rain.columns = cols

# Initializing a dataframe cotaining data about wind.    
    cols = pd.MultiIndex.from_product([['Wind'],['Avg. Vel.','Máx. Vel.']])
    wind = pd.DataFrame()

# Storing the data and putting in the last row the mean and the max. value of the year. 
    wind['Avg. Vel.'] =  np.round(database['avg_vel'].iloc[i,2:].tolist() + [database['avg_vel'].iloc[i,2:].mean()],1)
    wind['Max. Vel.'] =  np.round(database['max_vel'].iloc[i,2:].tolist() + [database['max_vel'].iloc[i,2:].max()],1)
#    vel_med_anual = database['vel_Med'].iloc[i,2:].mean()
#    vel_max = database['vel_Max'].iloc[i,2:].max()

    wind.columns = cols

# Initializing a dataframe with moisture information.
    moisture_df = pd.DataFrame(columns=['    Avg. Raltive \n Moisture'])
    moisture_df['    Avg. Relative \n Moisture.'] = np.round(database['moisture'].iloc[i,2:].tolist() + [database['moisture'].iloc[i,2:].mean()],1)    
    
    lst = np.round(database['dew_T'].iloc[i,2:].tolist() + [database['dew_T'].iloc[i,2:].mean()],1)
    dew_T = pd.DataFrame(lst, columns=['    Avg. Relative\n Moisture.'])
    
    return heliophany,pres,rain,wind,moisture_df,station

def station_temps_for_curves(extr_T: pd.DataFrame, avg_T: pd.DataFrame) -> pd.DataFrame:

# Storing temperature data into a dataframe that will be used for temperature curves.
    data = pd.DataFrame(columns=['Min.','Mean','Max.']) 
    data['Min.'], data['Mean'], data['Max.']= extr_T[[('Extremes', 'Min.')]], avg_T[[('Means', 'Avg.')]], extr_T[[('Extremes', 'Max.')]]
    
    return data

def rainfall_data(database: dict, i: int) -> pd.DataFrame:

# Storing rainfall data into a dataframe that will be used for the rainfall barplot.
    data = pd.DataFrame(columns=['Total','Normal'])    
    data['Total'], data['Normal']= database['rainfall'].iloc[i,2:], database['normal_rainfall'].iloc[i,2:]

    return data
