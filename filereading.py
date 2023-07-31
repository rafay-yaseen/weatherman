import os
import weatherdata

def read_data_from_file_year(directory, year):
    weather_data_list = []
    file_name = "Murree_weather_"+year
    for filename in os.listdir(directory):
        if file_name in filename:
            with open(os.path.join(directory, filename)) as file:
                file.readline()
                for line in file:
                    list = line.split(",")
                    weather_data_list.append(weatherdata.WeatherData(
                        list[0], list[1], list[2], list[3], list[7], list[8], list[9]))
    return weather_data_list


def read_data_from_file_month(directory, month, dict):
    weather_data_list = []
    list_month = month.split("/")
    month_name = list_month[1]
    month_name = int(month_name)
    file_name = "Murree_weather_"+list_month[0]+"_" + dict.get(month_name)
    for filename in os.listdir(directory):
        if file_name in filename:
            with open(os.path.join(directory, filename)) as file:
                file.readline()
                for line in file:
                    list = line.split(",")
                    weather_data_list.append(weatherdata.WeatherData(
                        list[0], list[1], list[2], list[3], list[7], list[8], list[9]))
    return weather_data_list
