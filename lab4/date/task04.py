import datetime

def date_difference_seconds(date1, date2):
    timedelta = date2 - date1
    difference_seconds = timedelta.total_seconds()
    return difference_seconds

date_str1 = input("First date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

difference_seconds = date_difference_seconds(date1, date2)

print(difference_seconds)
