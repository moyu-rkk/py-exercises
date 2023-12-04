# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list =data["temp"].to_list()
# print(len(temp_list))
# 转成raw py object了所以能用list method

# More series method
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns using bracket or dot notation
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# Get certain value from a row
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a DataFrame from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# grades = pandas.DataFrame(data_dict)
# grades.to_csv("grades.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231130.csv")
fur_colors = data["Primary Fur Color"].dropna().unique()
fur_numbers = data["Primary Fur Color"].dropna().value_counts()
fur_nums_new = fur_numbers.reset_index()
fur_nums_new.columns = ["Primary Fur Colors", "Count"]
squirrels_fur = pandas.DataFrame(fur_nums_new)
print(squirrels_fur)

# Angela's solution using fundamental methods but you have to know how many unique fur colors in advance
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# data_squirrels = {
#     "Primary Fur Color": ["Gary", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# df = pandas.DataFrame(data_squirrels)
# print(df)