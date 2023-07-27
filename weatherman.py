import argparse
import os


class WeatherData:
    date = 0
    max_temp = 0
    mean_temp = 0
    min_temp = 0
    max_humidity = 0
    mean_humidity = 0
    min_humidity = 0

    def __init__(self, date, max_temp, mean_temp, min_temp, max_humidity, mean_humidity, min_humidity):
        self.date = date
        self.max_temp = max_temp
        self.mean_temp = mean_temp
        self.min_temp = min_temp
        self. max_humidity = max_humidity
        self. mean_humidity = mean_humidity
        self. min_humidity = min_humidity


class WeatherCalculation:
    highest_temp = float('-inf')
    lowest_temp = float('inf')
    most_humidity = 0
    highest_temp_date = 0
    lowest_temp_date = 0
    most_humidity_date = 0
    lowest_average_temp = 0
    highest_average_temp = 0
    average_mean_humidity = 0

    def __init__(self):
        highest_temp = 0
        lowest_temp = 0
        most_humidity = 0
        highest_temp_date = 0
        lowest_temp_date = 0
        most_humidity_date = 0
        lowest_average_temp = 0
        highest_average_temp = 0
        average_mean_humidity = 0


def read_data_from_file_year(directory, year):
    weather_data_list = []
    file_name = "Murree_weather_"+year
    for filename in os.listdir(directory):
        if file_name in filename:
            with open(os.path.join(directory, filename)) as file:
                file.readline()
                for line in file:
                    list = line.split(",")
                    weather_data_list.append(WeatherData(
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
                    weather_data_list.append(WeatherData(
                        list[0], list[1], list[2], list[3], list[7], list[8], list[9]))
    return weather_data_list


def weather_calculation(relevant_data):
    weather_stats = WeatherCalculation()
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
    weather_data_list = read_data_from_file_year(directory, year)
    weather_stats = weather_calculation(weather_data_list)
    print("Max temp :", weather_stats.highest_temp,
          "C on", weather_stats.highest_temp_date)
    print("Min temp:", weather_stats.lowest_temp,
          "C on", weather_stats.lowest_temp_date)
    print("Most Humidity :", weather_stats.most_humidity,
          "%", "on ", weather_stats.most_humidity_date)


def month_report(directory, month, dict):
    weather_data_list = read_data_from_file_month(directory, month, dict)
    weather_stats = weather_calculation(weather_data_list)
    print("Highest Average:", int(weather_stats.highest_average_temp), "C")
    print("Lowest Average:", int(weather_stats.lowest_average_temp), "C")
    print("Average Mean Humidity :", int(
        weather_stats.average_mean_humidity), "%")


def chart_report(directory, month, dict):
    weather_data_list = read_data_from_file_month(directory, month, dict)
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


def main():

    MONTH_NUMBER_TO_NAME = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "directory", help="Path to the directory that contains weather file")
    ap.add_argument(
        "-a", "--month", help="Given month display the average highest temperature, average lowest temperature, average mean humidity.")
    ap.add_argument(
        "-e", "--year", help="Given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.")
    ap.add_argument("-c", "--chart", help="Given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.")

    args = ap.parse_args()

    if args.year:
        print("Year is entered")
        year_report(args.directory, args.year)
    if args.month:
        print("Month is entered")
        month_report(args.directory, args.month, MONTH_NUMBER_TO_NAME)
    if args.chart:
        print("Chart is entered")
        chart_report(args.directory, args.chart, MONTH_NUMBER_TO_NAME)


if __name__ == "__main__":
    main()
