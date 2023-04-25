# # csv -> comma seperated value(엑셀 표)
# import csv
import pandas

#
# with open("weather_data.csv") as data_file:
#     # weather_list = csv.readlines()
#     data = csv.reader(data_file)
#     temperature = []
#     for temp in data:
#         if temp[1] != "temp":
#             temperature.append(int(temp[1]))
#
#     print(temperature)


data = pandas.read_csv("weather_data.csv")
print(type(data))

print(data["temp"])
