# # # # Data Type
# # # # print("hello"[4])
# # # # a = 123_456_789


# # # # 🚨 Don't change the code below 👇
# # # two_digit_number = input("Type a two digit number: ")
# # # # 🚨 Don't change the code above 👆

# # # ####################################
# # # # Write your code below this line 👇
# # # print(int(two_digit_number[0]) + int(two_digit_number[1]))

# # # ** => 거듭제곱
# # # print(2 ** 3)
# # # / -> flaat
# # # () -> ** -> * , / -> + , -

# # # 🚨 Don't change the code below 👇
# # height = input("enter your height in m: ")
# # weight = input("enter your weight in kg: ")
# # # 🚨 Don't change the code above 👆


# # # Write your code below this line 👇
# # print(int(float(weight) / (float(height) ** 2)))

# # print(round(8 / 3, 2))
# # print(8 // 3) -> floor(버림)

# # score = 0

# # #Whenever users get score

# # score += 1
# score = 0
# # f-string
# print(f"You've got {score}")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
year_left = 90 - int(age)
month = year_left * 12
week = year_left * 52
days = year_left * 365

print(f"You have {days} days, {week} weeks, and {month} months left.")
