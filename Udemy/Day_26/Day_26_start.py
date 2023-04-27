# # # # # # list comprehension
# # # # # # make list with another list
# # # # #
# # # # # list = [1, 2, 3]
# # # # # new_list = [item + 1 for item in list]
# # # # #
# # # # # name = "yigang"
# # # # # new_string = [letter for letter in name]
# # # # #
# # # # # range_list = [item * 2 for item in range(1, 5)]
# # # # #
# # # # # if_list = [new_list for item in range(1, 100) if item % 2 == 0]
# # # # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # # # 🚨 Do Not Change the code above 👆
# # # #
# # # # #Write your 1 line code 👇 below:
# # # #
# # # # squared_numbers = [num **2 for num in numbers]
# # # #
# # # # #Write your code 👆 above:
# # # #
# # # # print(squared_numbers)
# # # #
# # # #
# # # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # # 🚨 Do Not Change the code above
# # #
# # # #Write your 1 line code 👇 below:
# # #
# # # result = [num for num in numbers if num % 2 == 0]
# # #
# # # #Write your code 👆 above:
# # #
# # # print(result)
# #
# #
# #
# # # dict_comprehension
# # import random
# #
# # dict = {
# #     "a": 10,
# #     "b": 20,
# #     "c": 40,
# #     "d": 60
# # }
# #
# # score = {student: "Pass" for (student, score) in dict.items() if score > 30} # if score > 30}
# #
# # print(score)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {keyword : len(keyword) for keyword in sentence.split(" ")}
#
# print(result)
#

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

# weather_f = {day_c : (temp_c * 9/5) + 32 for (day_c, temp_c) in weather_c.items()}
#
#
# print(weather_f)

import pandas

weather_df = pandas.DataFrame(index=[0], data=weather_c)

# for (key, value) in weather_df.items():
#     print(value)
#
for (index, value) in weather_df.iterrows():
    print(index)
