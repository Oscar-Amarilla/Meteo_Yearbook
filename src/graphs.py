import pandas as pd

import os

import seaborn as sns

import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator

from config import OUTPUT_DIR, DMH_LOGO_DIR, DINAC_LOGO_DIR  

from PIL import Image

def temps_curves(data: pd.DataFrame, months: pd.DataFrame, station: pd.Series):

# Setting the output directory. Create if it does not exist.
                os.makedirs(OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_'),  exist_ok=True)

# Setting plot properties. 
                sns.set_theme()
                fig_size = (12, 5)
                plt.figure(figsize=fig_size)
                ax=sns.lineplot(data=data, palette=['blue','gray','red'], linewidth=1.5)
                dimensiones = (168, 72)

# Importing logos.
                logo_1 = Image.open(DMH_LOGO_DIR).resize(dimensiones)
                logo_2 = Image.open(DINAC_LOGO_DIR).resize(dimensiones)

# Placing the logos in the plot.
                x_logo_2 = int(fig_size[0]*(1-0.308)*100)
                y_logo = int(fig_size[1]*(1-0.0125)*100)
                ax.figure.figimage(logo_1, x_logo_2*0.018, y_logo, zorder=1)
                ax.figure.figimage(logo_2, x_logo_2, y_logo, zorder=1)

# Placing data (boxes) in the plot. 
                box=dict(boxstyle="round", ec="white", fc="white",pad=0.1)
                for i in range(12):
                                plt.text(i, data['Min.'][i], data['Min.'][i], ha='center', size='medium', weight='semibold', bbox=box)

                for i in range(12):
                                plt.text(i, data['Mean'][i], data['Mean'][i], ha='center', size='medium', weight='semibold', bbox=box)

                for i in range(12):
                                plt.text(i, data['Max.'][i], data['Max.'][i], ha='center', size='medium', weight='semibold', bbox=box)

# Placing the legend box
                ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)

# Configuring axis.
                ax.set_xticks(range(len(months)))
                ax.set_xticklabels(months['Month'])
                plt.xlabel(None)
                plt.ylabel("Temperature (ºC)")

# Setting titles and legends.
                plt.title('\nTemperatures\n\n', fontsize=18)
                plot_title = station.Station + ', Department of ' + station.Department + '\nYear 2022\n'
                plt.suptitle(plot_title, fontsize=12)

# Saving the plot.
                path = OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_') + '/' + 'Temperatures-' + station.Station.replace('.','_').replace(' ','_')
                ax.figure.savefig(path, bbox_inches='tight')

def min_categorical_T_histo(data, months,station):

# Setting the output directory. Create if it does not exist.
                os.makedirs(OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_'),  exist_ok=True)

# Setting plot properties. 
                valor_max = max(data.max())
                fig_size = (12, 5)
                fig, ax = plt.subplots(figsize=(20, 10))
                data.plot.bar(ax=ax, width=0.7, figsize=fig_size, color=['lightsteelblue','cornflowerblue'] )
                dimensiones = (168, 72)

# Importing logos.
                logo_1 = Image.open(DMH_LOGO_DIR).resize(dimensiones)
                logo_2 = Image.open(DINAC_LOGO_DIR).resize(dimensiones)

# Placing the logos in the plot.
                x_logo_2 = int(fig_size[0]*(1-0.308)*100)
                y_logo = int(fig_size[1]*(1-0.0125)*100)
                ax.figure.figimage(logo_1, x_logo_2*0.018, y_logo, zorder=1)
                ax.figure.figimage(logo_2, x_logo_2, y_logo, zorder=1)

# Placing data (boxes) in the plot. 
                for i in range(12):
                        plt.text(i-0.18, data.iloc[i,0] + valor_max*0.025, data.iloc[i,0], rotation = 0, ha='center', size='medium', weight='semibold', color="black") 

                for i in range(12):
                        plt.text(i+0.18, data.iloc[i,1] + valor_max*0.025, data.iloc[i,1], rotation = 0, ha='center', size='medium', weight='semibold', color="black")

# Configuring axis.
                ax.set_xticks(range(len(months)))
                ax.set_xticklabels(months['Month'])
                plt.xticks(rotation=0)
                plt.xlabel(None)
                plt.ylabel('Number of days')
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))
                ax.set_ylim(top=valor_max*1.25)
# Setting titles and legends.
                ax.legend(['T \u2264 0ºC', '0ºC \u2264 T \u2264 5ºC'], loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
                plt.title('\nTemperatures\n\n', fontsize=18)
                plt.suptitle(station.Station + ', Department of ' + station.Department + '\nYear 2022\n', fontsize=12)

# Saving the image.
                path = OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_') + '/' + 'min_T-' + station.Station.replace('.','_').replace(' ','_')
                ax.figure.savefig(path, bbox_inches='tight')

def max_categorical_T_histo(data,months, station):
    
# Setting the output directory. Create if it does not exist.
                os.makedirs(OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_'),  exist_ok=True)

# Setting plot properties. 
                valor_max = max(data.max())
                fig_size = (12, 5)
                fig, ax = plt.subplots(figsize=(20, 10))
                data.plot.bar(ax=ax, width=0.8, figsize=fig_size, color=['indianred','firebrick'] )
                dimensiones = (168, 72)

# Importing logos.
                logo_1 = Image.open(DMH_LOGO_DIR).resize(dimensiones)
                logo_2 = Image.open(DINAC_LOGO_DIR).resize(dimensiones)

# Placing the logos in the plot.
                x_logo_2 = int(fig_size[0]*(1-0.308)*100)
                y_logo = int(fig_size[1]*(1-0.0125)*100)
                ax.figure.figimage(logo_1, x_logo_2*0.018, y_logo, zorder=1)
                ax.figure.figimage(logo_2, x_logo_2, y_logo, zorder=1)

# Placing data (boxes) in the plot. 
                for i in range(12):
                        plt.text(i-0.18, data.iloc[i,0] + valor_max*0.025, data.iloc[i,0], rotation = 0, ha='center', size='medium', weight='semibold', color="black") 
                for i in range(12):
                        plt.text(i+0.18, data.iloc[i,1] + valor_max*0.025, data.iloc[i,1], rotation = 0, ha='center', size='medium', weight='semibold', color="black")

# Configuring axis.
                ax.set_xticks(range(len(months)))
                ax.set_xticklabels(months['Month'])
                plt.xticks(rotation=0)
                plt.xlabel(None)
                plt.ylabel('Number of days')
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))
                ax.set_ylim(top=valor_max*1.25)
                
# Setting titles and legends.
                ax.legend(['35ºC \u2264 T \u2264 40ºC', 'T \u2265 40ºC'], loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
                plt.title('\nTemperatures\n\n', fontsize=18)
                plt.suptitle(station.Station + ', Department of ' + station.Department + '\nYear 2022\n', fontsize=12)
 
# Saving the image.
                path = OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_') + '/' + 'max_T-' + station.Station.replace('.','_').replace(' ','_')
                fig.savefig(path, bbox_inches='tight')

def rainfall_histo(data, months, station):

# Setting the output directory. Create if it does not exist.
                os.makedirs(OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_'),  exist_ok=True)

# Setting plot properties. 
                valor_max = max(data.max())
                fig_size = (12, 5)
                fig, ax = plt.subplots(figsize=(20, 10))
                data.plot.bar(ax=ax, width=0.8, figsize=fig_size, color=['mediumaquamarine','green'] )
                dimensiones = (168, 72)

# Importing logos.
                logo_1 = Image.open(DMH_LOGO_DIR).resize(dimensiones)
                logo_2 = Image.open(DINAC_LOGO_DIR).resize(dimensiones)


# Placing the logos in the plot.
                x_logo_2 = int(fig_size[0]*(1-0.308)*100)
                y_logo = int(fig_size[1]*(1-0.0125)*100)
                ax.figure.figimage(logo_1, x_logo_2*0.018, y_logo, zorder=1)
                ax.figure.figimage(logo_2, x_logo_2, y_logo, zorder=1)

# Placing data (boxes) in the plot. 
                box=dict(boxstyle="larrow", ec="white", fc='skyblue',pad=0.1)
                for i in range(12):
                                plt.text(i-0.2, data.Total[i] + valor_max*0.05, data.Total[i], rotation = 90, ha='center', size='medium', weight='semibold', color="black")    
                for i in range(12):
                                plt.text(i+0.225, data.Normal[i] + valor_max*0.05, data.Normal[i], rotation = 90, ha='center', size='medium', weight='semibold', color="black")        

# Configuring axis.
                ax.set_xticklabels(months['Month'])
                plt.xticks(rotation=0)
                plt.xlabel(None)
                plt.ylabel('Rainfall (mm)')
                ax.set_ylim(top=valor_max*1.25)

# Setting titles and legends.
                ax.legend(['Total', 'Normal*'], loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
                ax.text(8, -valor_max*0.25, '*With respect to the period 1991-2020', size='small', weight='light', color="black")        
                plt.title('\nMonthly Rainfall\n\n', fontsize=18)
                plt.suptitle(station.Station + ', Department of ' + station.Department + '\nYear 2022\n', fontsize=12)

# Saving the image.
                path = OUTPUT_DIR + '/' + station.Station.replace('.','_').replace(' ','_') + '/' + 'Rainfall-' + station.Station.replace('.','_').replace(' ','_')
                fig.savefig(path, bbox_inches='tight')
