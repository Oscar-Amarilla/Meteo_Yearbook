"""This script extract data from CSV files in the input directory and places them into 

data frames that will remain in the working environment."""

from pathlib import Path

import pandas as pd

from pandas.errors import ParserError

def extract_and_load(input_dir, csv_dataframe_mapping):

    dataframes = {}
   
# A try/except line in setted in order to avoid problems with delimiters.
    for csv_file, table_name in csv_dataframe_mapping.items():  

        try:
            
            dataframes[table_name]= pd.read_csv(f"{input_dir}/{csv_file}", delimiter=",")
        
        except ParserError as err:
        
            dataframes[table_name]= pd.read_csv(f"{input_dir}/{csv_file}", delimiter=";")

# Dataframe with the month of the year. The last entry is "Anual", this is for the summary information row of the tables.
    month = pd.DataFrame(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Annual"], columns=["Month"])

    return dataframes, month
