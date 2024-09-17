import argparse
from weatherman_packages import constants
from weatherman_packages import weatherman

def main():

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
        weatherman.year_report(args.directory, args.year)
    if args.month:
        print("Month is entered")
        weatherman.month_report(args.directory, args.month, constants.Month)
    if args.chart:
        print("Chart is entered")
        weatherman.chart_report(args.directory, args.chart, constants.Month)

if __name__ == "__main__":
    main()
