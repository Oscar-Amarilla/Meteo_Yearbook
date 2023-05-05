import os

import pandas as pd

import numpy as np

from numpy import NaN, nan

from typing import Union

import textwrap

from pandas.plotting import table

import matplotlib.pyplot as plt

from PIL import Image,ImageDraw,ImageFont

from config import OUTPUT_DIR, FONT_DIR 

import warnings

warnings.filterwarnings("ignore")

warnings.simplefilter("ignore")


def center(text:str, del_x:float, font:object) -> float:
    
    text_len = font.getsize(str(text))[0]
    
    margin = abs(del_x-text_len)/2
    
    return margin

def nan2SD(data:Union[int,float,str]) -> str:

    if str(data) in ['nan', 'NaN']:

        return 'SD'

    else:

        return str(data)

def variables_table(months:pd.DataFrame,heliophany:pd.DataFrame,pres:pd.DataFrame,rainfall:pd.DataFrame,wind:pd.DataFrame,moisture_df:pd.DataFrame,station:pd.Series):

    os.makedirs(OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_'),  exist_ok=True)

# Initializing the image
    img = Image.new('RGB', (1500, 420), color='white')
    new_size = (1125, 315) # Output size of the table. 
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_DIR, 18)

    # Define color properties
    header_color = (211, 211, 211)
    grid_color = 'black'

# Defining the lenght of a cell.
    del_x = 140
    #------------- Month column -------------------
    df = months

# Defining the lenght of a cell.
    dx_1 = 85

# Headers
    x_offset = 25
    y_offset = 25
    header=df.columns[0]
    draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 50), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1, font), y_offset + 15), header, font=font, fill='black')

# Draw table data
    x_offset = 25
    y_offset = 75
    for i in range(len(df)):
        row = list(df.iloc[i]) 
        for j in range(len(row)):
            dato = nan2SD(row [j])     
            draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, dx_1, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += dx_1
        x_offset = 25
        y_offset += 25

#------------- Heliophany -------------------
    df = heliophany

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

# Headers
    x_offset = 25 + dx_1
    y_offset = 25
    header=df.columns[0][0]
    draw.rectangle((x_offset, y_offset, x_offset + dx_1*2, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1*2, font), y_offset +2.5), header, font=font, fill='black')
    x_offset += del_x

# Draw table headers
    headers = list(columns)
    x_offset = dx_1 + 25
    y_offset = 50
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset+ center(header, dx_1, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += dx_1

# Draw table data
    x_offset = dx_1 + 25
    y_offset = 75
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, dx_1, font), y_offset + 2.5), dato, font=font, align ="center", fill='black')
            x_offset += dx_1
        x_offset =  dx_1 + 25
        y_offset += 25

# Draw grid lines
    x_offset = del_x + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = del_x + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10 

#--------------- Preassure ----------------------
    df = pres

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

    #Class header
    x_offset = dx_1*3 + 25
    y_offset = 25
    header=df.columns[0][0]
    draw.rectangle((x_offset, y_offset, x_offset + del_x*2.4, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, del_x*2.4, font), y_offset +2.5), header, font=font, fill='black')

# Draw table headers
    headers = list(columns)
    x_offset = dx_1*3 + 25
    y_offset = 50
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + del_x*1.2, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset + center(header, del_x*1.2, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += del_x*1.2

# Draw table data
    x_offset = dx_1*3 + 25
    y_offset = 75
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + del_x*1.2, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, del_x*1.2, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += del_x*1.2
        x_offset = dx_1*3 + 25
        y_offset += 25

# Draw grid lines
    x_offset = del_x*3 + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = del_x*3 + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10   

#--------------- Rainfall ----------------------
    df = rainfall

    dx_2 = dx_1*3 + del_x*2.4

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

# Headers
    x_offset = dx_2 + 25
    y_offset = 25
    header=df.columns[0][0]
    draw.rectangle((x_offset, y_offset, x_offset + del_x*4, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, del_x*4, font), y_offset +2.5), header, font=font, fill='black')

# Draw table headers
    headers = list(columns)
    x_offset = dx_2 + 25
    y_offset = 50
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset + center(header, del_x, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += del_x

# Draw table data
    x_offset = dx_2 + 25
    y_offset = 75
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, del_x, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += del_x
        x_offset = dx_2 + 25
        y_offset += 25

# Draw grid lines
    x_offset = dx_2 + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = dx_2 + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10   

#---------------- Wind ---------------------
    df = wind

    dx_3 = dx_2 + del_x*4

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

# Headers
    x_offset = dx_3 + 25
    y_offset = 25
    header=df.columns[0][0]
    draw.rectangle((x_offset, y_offset, x_offset + dx_1*2, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1*2, font), y_offset +2.5), header, font=font, fill='black')


# Draw table headers
    headers = list(columns)
    x_offset = dx_3 + 25
    y_offset = 50
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset + center(header, dx_1, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += dx_1

# Draw table data
    x_offset = dx_3 + 25
    y_offset = 75
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, dx_1, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += dx_1
        x_offset = dx_3 + 25
        y_offset += 25

# Draw grid lines
    x_offset = dx_3 + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = dx_3 + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10

#-------------- Moisture -----------------------
    df = moisture_df

    dx_4 = dx_3 + 2*dx_1

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

# Headers
    x_offset = dx_4 + 25
    y_offset = 25
    header='Avg. Relative\n    Moisture'
    draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 50), fill=header_color, outline=grid_color)
    draw.text((x_offset + center('Avg. Relative', del_x, font), y_offset + 5), header, font=font, fill='black')
    x_offset += dx_1

# Draw table data
    x_offset = dx_4 + 25
    y_offset = 75
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, del_x, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += dx_1
        x_offset = dx_4 + 25
        y_offset += 25

# Draw grid lines
    x_offset = dx_4 + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    

    img = img.resize(new_size, resample=Image.LANCZOS, reducing_gap=3.0)
    
    path = OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_') + '/' + 'Variables_table-' + station.Station.replace('.','_').replace(' ','_') + '.png'

# Save the image
    img.save(path, quality=95)

    display(img)

def temps_table(months:pd.DataFrame,extr_T:pd.DataFrame,avg_T:pd.DataFrame,cate_T:pd.DataFrame,dew_T:pd.DataFrame,station:pd.Series):

    os.makedirs(OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_'),  exist_ok=True)

# Initializing the image
    img = Image.new('RGB', (1320, 450), color='white')
    new_size = (987, 337) # Output size of the table. 
    draw = ImageDraw.Draw(img)
    
    font_header = ImageFont.truetype(FONT_DIR, 22)
    font = ImageFont.truetype(FONT_DIR, 18)

# Defining color properties
    header_color = (211, 211, 211)
    grid_color = 'black'

# Cell lengths
    del_x = 130
    dx_1 = 80

# Header
    x_offset = 25
    y_offset = 20
    header='Temperature (ºC)'
    draw.rectangle((x_offset, y_offset, x_offset + dx_1*8 + del_x*5, y_offset + 30), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1*8 + del_x*5, font), y_offset + 2), header, font=font_header, fill='black')

#------------- Months columns -------------------
    df = months

# Headers
    x_offset = 25
    y_offset = 50
    header=df.columns[0]
    draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 50), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1, font), y_offset + 15), header, font=font, fill='black')

# Draw table data
    x_offset = 25
    y_offset = 100
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=(255, 255, 255), outline='black')
            draw.text((x_offset + center(dato, dx_1, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += dx_1
        x_offset = 25
        y_offset += 25

#------------- Extreme temperatures -------------------
    df = extr_T

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

# Class header
    x_offset = 25 + dx_1
    y_offset = 50
    header=df.columns[0][0]
    draw.rectangle((x_offset, y_offset, x_offset + dx_1*4, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1*4, font), y_offset +2.5), header, font=font, fill='black')
    x_offset += del_x


# Draw table headers
    headers = list(columns)
    x_offset = dx_1 + 25
    y_offset = 75
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset+ center(header, dx_1, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += dx_1

# Draw table data
    x_offset = dx_1 + 25
    y_offset = 100
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, dx_1, font), y_offset + 2.5), dato, font=font, align ="center", fill='black')
            x_offset += dx_1
        x_offset =  dx_1 + 25
        y_offset += 25

# Draw grid lines
    x_offset = del_x + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = del_x + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10 
#----------------- Means --------------------
    df = avg_T

    columns = []

    for i in range(len(df.columns)):

        columns.append(df.columns[i][1])

# Class header
    x_offset = dx_1*5 + 25
    y_offset = 50
    header=df.columns[0][0]
    draw.rectangle((x_offset, y_offset, x_offset + dx_1*3, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, dx_1*3, font), y_offset +2.5), header, font=font, fill='black')


# Draw table headers
    headers = list(columns)
    x_offset = dx_1*5 + 25
    y_offset = 75
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset + center(header, dx_1, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += dx_1

# Draw table data
    x_offset = dx_1*5 + 25
    y_offset = 100
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + dx_1, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, dx_1, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += dx_1
        x_offset = dx_1*5 + 25
        y_offset += 25

# Draw grid lines
    x_offset = del_x*3 + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = del_x*3 + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10   

#----------------- Categorical temperatures --------------------
    df = cate_T

    dx_2 = dx_1*8

    #Class header
    x_offset = dx_2 + 25
    y_offset = 50
    header='Number of Events'
    draw.rectangle((x_offset, y_offset, x_offset + del_x*4, y_offset + 25), fill=header_color, outline=grid_color)
    draw.text((x_offset + center(header, del_x*4, font), y_offset +2.5), header, font=font, fill='black')
        
# Draw table headers
    headers = df.columns
    x_offset = dx_2 + 25
    y_offset = 75
    for header in headers:
        draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 25), fill=header_color, outline=grid_color)
        draw.text((x_offset + center(header, del_x, font), y_offset + 2.5), header, font=font, fill='black')
        x_offset += del_x

# Draw table data
    x_offset = dx_2 + 25
    y_offset = 100
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, del_x, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += del_x
        x_offset = dx_2 + 25
        y_offset += 25

# Draw grid lines
    x_offset = dx_2 + 25
    y_offset = 50
    for i in range(len(df) + 1):
        draw.line((x_offset, y_offset, x_offset, y_offset), fill=grid_color, width=1)
        y_offset += 50

    x_offset = dx_2 + 25
    y_offset = 50
    for i in range(len(df.columns) + 1):
        draw.line((x_offset, y_offset, x_offset + 20, y_offset), fill=grid_color, width=1)
        x_offset += 10   

#--------------- Dew point temperature ----------------------
    df = dew_T
    dx_3 = dx_2 + del_x*4

    columns = []

# Draw table headers
    header = '  Dew Point \nTemperature'
    x_offset = dx_3 + 25
    y_offset = 50

    draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 50), fill=header_color, outline=grid_color)
    draw.text((x_offset + center('Temperature', del_x, font), y_offset + 5), header, font=font, fill='black')
    x_offset += dx_1

# Draw table data
    x_offset = dx_3 + 25
    y_offset = 100
    for i in range(len(df)):
        row = list(df.iloc[i])
        for j in range(len(row)):
            dato = nan2SD(row [j])
            draw.rectangle((x_offset, y_offset, x_offset + del_x, y_offset + 25), fill=(255, 255, 255), outline=grid_color)
            draw.text((x_offset + center(dato, del_x, font), y_offset + 2.5), dato, font=font, fill='black')
            x_offset += dx_1
        x_offset = dx_3 + 25
        y_offset += 25


    img = img.resize(new_size, resample=Image.LANCZOS, reducing_gap=3.0)
    
    path = OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_') + '/' + 'Temperatures_table-' +  station.Station.replace('.','_').replace(' ','_') + '.png'

# Save the image
    img.save(path, quality=95)

    display(img)

