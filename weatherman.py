import argparse
import os


class WeatherData:
    date = 0
    max_temp = 0
    mean_temp=0
    min_temp=0
    max_humidity=0
    mean_humidity=0
    min_humidity=0


    def __init__(self, date,max_temp,mean_temp,min_temp,max_humidity,mean_humidity,min_humidity):
      self.date = date
      self.max_temp = max_temp
      self.mean_temp=mean_temp
      self.min_temp=min_temp
      self. max_humidity=max_humidity
      self. mean_humidity=mean_humidity
      self. min_humidity=min_humidity

class WeatherCalculation:
        highest_temp=float('-inf')
        lowest_temp=float('inf')
        most_humidity=0
        highest_temp_date=0
        lowest_temp_date=0
        most_humidity_date=0
        lowest_average_temp=0
        highest_average_temp=0
        average_mean_humidity=0

        def __init__(self):
         highest_temp=0
         lowest_temp=0
         most_humidity=0
         highest_temp_date=0
         lowest_temp_date=0
         most_humidity_date=0
         lowest_average_temp=0
         highest_average_temp=0
         average_mean_humidity=0
    


def read_data_from_file(directory,year):
    weather_data_list = []
    file_name="Murree_weather_"+year
    for filename in os.listdir(directory):
        if file_name in filename:
            with open(os.path.join(directory, filename)) as file:
                file.readline()
                for line in file:
                    list=line.split(",")
                    weather_data_list.append(WeatherData(list[0],list[1],list[2],list[3],list[7],list[8],list[9]))
    return weather_data_list


def weather_calculation(relevant_data):
    weather_stats=WeatherCalculation()
    total_max_temp=0
    total_min_temp=0
    total_humidity=0
    no_of_days=0
    for reading in relevant_data:
        if reading.max_temp !="":
           total_max_temp += float(reading.max_temp)
           if float(reading.max_temp) >float(weather_stats.highest_temp):
               weather_stats.highest_temp=reading.max_temp
               weather_stats.highest_temp_date=reading.date
           
        if reading.min_temp !="":
             total_min_temp+=float(reading.min_temp)
             if float(reading.min_temp)<float(weather_stats.lowest_temp):
                weather_stats.lowest_temp=reading.min_temp
                weather_stats.lowest_temp_date=reading.date
    
        if reading.max_humidity !="":
            total_humidity += float(reading.mean_humidity)
            if float(reading.max_humidity)>float(weather_stats.most_humidity):
               weather_stats.most_humidity=reading.max_humidity
               weather_stats.most_humidity_date=reading.date
        no_of_days += 1


    weather_stats.highest_average_temp=total_max_temp/no_of_days
    weather_stats.lowest_average_temp=total_min_temp/no_of_days
    weather_stats.average_mean_humidity=total_humidity/no_of_days

    return weather_stats

def year_report(directory, year,dict):
    weather_data_list = read_data_from_file(directory,year)
    weather_stats=weather_calculation(weather_data_list)
    print("Max temp :",weather_stats.highest_temp,"C on",weather_stats.highest_temp_date)
    print("Min temp:",weather_stats.lowest_temp,"C on",weather_stats.lowest_temp_date)
    print("Most Humidity :",weather_stats.most_humidity,"%", "on ",weather_stats.most_humidity_date)

def main():

    MONTH_NUMBER_TO_NAME = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
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
        year_report(args.directory,args.year,MONTH_NUMBER_TO_NAME)
    if args.month:
        print("Month is entered")
    if args.chart:
        print("Chart is entered")


if __name__ == "__main__":
    main()
