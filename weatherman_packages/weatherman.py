from weatherman_packages import constants
from weatherman_packages import filereading

def weather_calculation(relevant_data):
    weather_stats = constants.WeatherCalculation()
    total_max_temp = 0
    total_min_temp = 0
    total_humidity = 0
    no_of_days = 0
    for reading in relevant_data:
        if reading.max_temp != "":
            total_max_temp += float(reading.max_temp)
            if float(reading.max_temp) > float(weather_stats.highest_temp):
                weather_stats.highest_temp = reading.max_temp
                weather_stats.highest_temp_date = reading.date

        if reading.min_temp != "":
            total_min_temp += float(reading.min_temp)
            if float(reading.min_temp) < float(weather_stats.lowest_temp):
                weather_stats.lowest_temp = reading.min_temp
                weather_stats.lowest_temp_date = reading.date

        if reading.max_humidity != "":
            total_humidity += float(reading.mean_humidity)
            if float(reading.max_humidity) > float(weather_stats.most_humidity):
                weather_stats.most_humidity = reading.max_humidity
                weather_stats.most_humidity_date = reading.date
        no_of_days += 1

    weather_stats.highest_average_temp = total_max_temp/no_of_days
    weather_stats.lowest_average_temp = total_min_temp/no_of_days
    weather_stats.average_mean_humidity = total_humidity/no_of_days

    return weather_stats


def year_report(directory, year):
    weather_data_list = filereading.read_data_from_file_year(directory, year)
    weather_stats = weather_calculation(weather_data_list)
    print("Max temp :", weather_stats.highest_temp,
          "C on", weather_stats.highest_temp_date)
    print("Min temp:", weather_stats.lowest_temp,
          "C on", weather_stats.lowest_temp_date)
    print("Most Humidity :", weather_stats.most_humidity,
          "%", "on ", weather_stats.most_humidity_date)
    line="_"*50
    print(line)


def month_report(directory, month, Month):
    weather_data_list = filereading.read_data_from_file_month(directory, month, Month)
    weather_stats = weather_calculation(weather_data_list)
    print("Highest Average:", int(weather_stats.highest_average_temp), "C")
    print("Lowest Average:", int(weather_stats.lowest_average_temp), "C")
    print("Average Mean Humidity :", int(
        weather_stats.average_mean_humidity), "%")
    line="_"*50
    print(line)


def chart_report(directory, month,Month):
    weather_data_list = filereading.read_data_from_file_month(directory, month, Month)
    for reading in weather_data_list:
        max_temp = reading.max_temp
        min_temp = reading.min_temp
        day = reading.date.split("-")
        plus_signs = "\033[91m" + "+" * int(max_temp) + "\033[0m"
        print(day[2], " ", plus_signs, reading.max_temp, "C")
        plus_signs = None
        plus_signs = "\033[94m" + "+" * int(min_temp)+"\033[0m"
        print(day[2], " ", plus_signs, reading.min_temp, "C")

    print("///For Bonus Task////")
    for reading in weather_data_list:
        max_temp = reading.max_temp
        min_temp = reading.min_temp
        day = reading.date.split("-")
        plus_sign_red = "\033[91m" + "+" * int(max_temp) + "\033[0m"
        plus_sign_blue = "\033[94m" + "+" * int(min_temp)+"\033[0m"
        print(day[2], " ", plus_sign_red, plus_sign_blue,
              reading.min_temp, "C -", reading.max_temp, "C")
    line="_"*50
    print(line)
    