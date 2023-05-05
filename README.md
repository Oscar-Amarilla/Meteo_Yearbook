# [Meteo_Yearbook](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook)

by Oscar Amarilla, 2023

[Meteo_Yearbook](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook) is intended to summarize meteorological data of a year into  a series of graphs, barplots and tables. It takes different csv files containing each one data about a particular meteorological variable, organize and place them into charts and tables.

You are free to copy, modify, and distribute this proyect, even for commercial purposes, without asking for permission. Please adapt this proyect for your own needs even if your data has nothing to do with meteorology. See *[Public domain dedication](https://github.com/ddbeck/readme-checklist#public-domain-dedication)* for details.

## How does [Meteo_Yearbook](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook) works?

The project consist in a series of scripts that follows an **ELT** _(extract-load-transform)_ scheme to organize data about the main meteorological variables and place them into comprehensible charts.

The structure of the project is the following:

```
|--input/ (Input data and images(logos))
|
|--src/
|    |
|    |- config.py (Path to necessary files for the project and settings for the extract_and_load script)
|    |
|    |- extract.py (Process of extraction and load of data in the workspace)
|    |
|    |- transform.py (Creation of pandas dataframes with the data needed for each graph and table)
|    |
|    |- tables.py (Table generator)
|    |
|    |_ graphs.py (Curves and barplot generator)
|
|--font/
|    |
|    |_ arial.ttf (Typography for the tables)
|
|--notebook/
|    |
|    |- scr2nb.py (Allow to import scripts from scr directory as part of a module in the notebook)
|    |
|    |_ Graphs_and_tables_about_meteorological_variables.ipynb (A notebook that works as a visual pipeline of the project)
|
|__ requirements.txt
|
|__ README.md 
```

The input data is in the input directory, from where config.py, extract.py and transform.py scripts located in the src directory will do the ELT job. This project comes with "toy" data in order to allow the user to run it imidiately after pulling it and also to show how data must be organized to replicate the results.

The user may take a look at the notebook, where the project has been explained in further details an could be a little more easy to follow.

## How to run [Meteo_Yearbook](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook)?

First thing to do is to generate a python virtual enviornment in a bash terminal.
```bash
python -m venv here_goes_the_name_of_the_venv # The name of the venv is up to the user.
```
Activate the virtual enviorment
```bash
source name_of_the_venv/bin/activate
```
Then install the requirements listed in the requirements.txt using pip.
```bash
pip install -r requirements.txt
```
Then the project can be run in the notebook. In the terminal, go to the notebook directory and run the notebook and open it.
```bash
jupyter notebook
```
## Contributing to [Meteo_Yearbook](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook)

Every comment and/or suggestion for improving [Meteo_Yearbook](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook) will be very wellcome, so every user is coordially invated to [open an issue or pull request on GitHub](https://https://github.com/Oscar-Amarilla/Meteo_Yearbook).

## Public domain dedication

This work is dedicated to the [public domain (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, Oscar Amarilla has waived all copyright and related or neighboring rights to the README checklist. See the LICENSE file for all the legalese.
