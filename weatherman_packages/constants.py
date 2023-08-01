from enum import Enum

Month = Enum("Month", {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
})

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
    