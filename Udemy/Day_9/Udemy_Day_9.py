# # # # # # # dictionaries!
# # # # # # hashmap = dictionary
# # # # # {Key: value}
# # # # # {"Bug": "error",
# # # # #  "fruit": "good"
# # # # #  }

# # # # program_dic = {
# # # #     "bug": "error",
# # # #     "algo": "rithm"
# # # # }

# # # # print(program_dic["bug"])


# # # # program_dic["loop"] = "true"

# # # # print(program_dic["loop"])

# # # # empty_dic = {}
# # # # # program_dic.clear()
# # # # # print(program_dic)

# # # # program_dic["bug"] = "Fu*k"

# # # # # dic loop

# # # # for thing in program_dic:
# # # #     print(thing)  # key를 출력
# # # #     print(program_dic[thing])

# # # student_scores = {
# # #     "Harry": 81,
# # #     "Ron": 78,
# # #     "Hermione": 99,
# # #     "Draco": 74,
# # #     "Neville": 62,
# # # }
# # # # 🚨 Don't change the code above 👆

# # # # TODO-1: Create an empty dictionary called student_grades.
# # # student_grades = {}

# # # # TODO-2: Write your code below to add the grades to student_grades.👇
# # # for stu in student_scores:
# # #     if (student_scores[stu] > 90):
# # #         student_grades[stu] = "Outstanding"
# # #     elif (student_scores[stu] > 80):
# # #         student_grades[stu] = "Exceeds Expectations"
# # #     elif (student_scores[stu] > 70):
# # #         student_grades[stu] = "Acceptable"
# # #     else:
# # #         student_grades[stu] = "Fail"


# # # # 🚨 Don't change the code below 👇
# # # print(student_grades)

# # # Nesting = 중첩

# # {key : [List],
# #  key : {dict},
# #  }

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# # 🚨 Do NOT change the code above

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 👇


# def add_new_country(country, visits, cities):
#     travel_log.append({"country": country, "visits": visits, "cities": cities})


# # 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
