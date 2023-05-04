from pathlib import Path


INPUT_DIR = str(Path.cwd().parent / "input")

OUTPUT_DIR = str(Path.cwd().parent / 'outputs')

FONT_DIR = str(Path.cwd().parent / 'font/arial.ttf')

DMH_LOGO_DIR = str(Path.cwd().parent / 'input/logo_1.png')

DINAC_LOGO_DIR = str(Path.cwd().parent / 'input/logo_2.png')

def csv_to_dataframe_mapping():

    return dict(
            [
#----Precipitation data--------------------------
                ("rainfall.csv","rainfall"),
                ("normal_rainfall.csv", "normal_rainfall"),
                ("max_rainfall_in_24hs.csv","max_rainfall_24"),
                ("days_of_max_rainfall.csv","max_rainfall_24_day"),
                ("days_with_rainfall.csv","rainfall_days"),

#----Heliophany data--------------------------
                ("avg_heliophany.csv","avg_helio"),
                ("total_heliophany.csv","total_helio"),

#----Moisture data--------------------------
                ("moisture.csv","moisture"),


#----Atm. preassure data--------------------------
                ("qne.csv","qne"),
                ("qnh.csv","qnh"),


#----Temperature data--------------------------
                ("dew_T.csv","dew_T"),
                ("extr_Tmax.csv","max_T"),
                ("avg_Tmax.csv","avg_Tmax"),
                ("days_with_Tmax.csv","day_Tmax"),
                ("avg_T.csv","avg_T"),
                ("extr_Tmin.csv","min_T"),
                ("avg_Tmin.csv","avg_Tmin"),
                ("days_with_Tmin.csv","day_Tmin"),

#----Categorical temperature data--------------------------
                ("days_with_T0.csv","t_0"),
                ("days_with_T5_0.csv","t_0_5"),
                ("days_with_T35_40.csv","t_35_40"),
                ("days_with_T40.csv","t_40"),

#----Wind velocity data--------------------------
                ("max_vel.csv","max_vel"),
                ("avg_vel.csv", "avg_vel"),

#----Location data--------------------------
                ("location.csv","location"),
            ])

