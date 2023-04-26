# # # csv -> comma seperated value(엑셀 표)
# # import csv
# import pandas
#
# #
# # with open("weather_data.csv") as data_file:
# #     # weather_list = csv.readlines()
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for temp in data:
# #         if temp[1] != "temp":
# #             temperature.append(int(temp[1]))
# #
# #     print(temperature)
#
#
# data = pandas.read_csv("weather_data.csv")
#
# data_list = data["temp"].to_list()
#
# print(data["temp"].max())
# print(data.temp)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp * (9 / 5) + 32 )
#
#
# data_dict = {
#     "students" : ["a", "b", "c"],
#     "grade" : ["f", "d", "e"]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")
# print(data)

import pandas as pd

sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_list = sq_data["Primary Fur Color"].to_list()

gray_list = sq_data[sq_data["Primary Fur Color"] == "Gray"]

print(gray_list)

fur_dict = {
   "Fur Color": ["Gray", "Cinnamon", "Black"],
   "Count": [len(gray_list), fur_list.count("Cinnamon"), fur_list.count("Black")]
}
pd.DataFrame(fur_dict).to_csv("Central Park Squirrel")