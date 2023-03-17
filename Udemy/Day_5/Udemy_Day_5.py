# # # # # # # for loop

# # # # # # fruits = ["apple", "peach", "pear"]

# # # # # # for fruit in fruits:
# # # # # #     print(fruit)


# # # # # # 🚨 Don't change the code below 👇
# # # # # student_heights = input("Input a list of student heights ").split()
# # # # # for n in range(0, len(student_heights)):
# # # # #     student_heights[n] = int(student_heights[n])
# # # # # # 🚨 Don't change the code above 👆
# # # # # height_sum = 0

# # # # # for n in range(0, len(student_heights)):
# # # # #     height_sum += student_heights[n]

# # # # # print(round(height_sum / len(student_heights)))

# # # # # # Write your code below this row 👇

# # # # # # 🚨 Don't change the code below 👇
# # # # # student_scores = input("Input a list of student scores ").split()
# # # # # for n in range(0, len(student_scores)):
# # # # #     student_scores[n] = int(student_scores[n])
# # # # # print(student_scores)
# # # # # # 🚨 Don't change the code above 👆

# # # # # # Write your code below this row 👇
# # # # # max = 0

# # # # # for n in range(0, len(student_scores)):
# # # # #     if (student_scores[n] > max):
# # # # #         max = student_scores[n]

# # # # # print(f"The highest score in the class is: {max}")

# # # # range(1, 10)  # 10은 포함 안됨 1이상 10미만
# # # for num in range(1, 10, 3):  # 3씩 증가
# # #     print(num)

# # sum = 0
# # for even in range(2, 101, 2):
# #     sum += even
# # print(sum)

# for num in range(1, 101):
#     if (num % 15 == 0):
#         print("FizzBuzz")
#     elif (num % 3 == 0):
#         print("Fizz")
#     elif (num % 5 == 0):
#         print("Buzz")
#     else:
#         print(num)
