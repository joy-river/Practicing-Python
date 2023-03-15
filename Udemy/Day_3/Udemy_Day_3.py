# # # # # a = 1
# # # # # if a > 1 :
# # # # #     print("false")
# # # # # else :
# # # # #     print("true")

# # # # # 🚨 Don't change the code below 👇
# # # # number = int(input("Which number do you want to check? "))
# # # # # 🚨 Don't change the code above 👆

# # # # # Write your code below this line 👇
# # # # if number % 2 == 0:
# # # #     print("This is an even number.")
# # # # else:
# # # #     print("This is an odd number.")

# # # # 🚨 Don't change the code below 👇
# # # height = float(input("enter your height in m: "))
# # # weight = float(input("enter your weight in kg: "))
# # # # 🚨 Don't change the code above 👆
# # # # Write your code below this line 👇
# # # User_bmi = round(weight / height ** 2)
# # # if User_bmi < 18.5:
# # #     print(f"Your BMI is {User_bmi}, you are underweight.")
# # # elif User_bmi < 25:
# # #     print(f"Your BMI is {User_bmi}, you have a normal weight.")
# # # elif User_bmi < 30:
# # #     print(f"Your BMI is {User_bmi}, you are slightly overweight.")
# # # elif User_bmi < 35:
# # #     print(f"Your BMI is {User_bmi}, you are obese.")
# # # else:
# # #     print(f"Your BMI is {User_bmi}, you are clinically obese.")

# # # # 🚨 Don't change the code below 👇
# # # year = int(input("Which year do you want to check? "))
# # # # 🚨 Don't change the code above 👆

# # # # Write your code below this line 👇
# # # is_leaf = False

# # # if year % 4 == 0:
# # #     is_leaf = True
# # #     if year % 100 == 0:
# # #         is_leaf = False
# # #     if year % 400 == 0:
# # #         is_leaf = True

# # # if is_leaf:
# # #     print("Leap year.")
# # # else:
# # #     print("Not leap year.")

# # # 🚨 Don't change the code below 👇
# # print("Welcome to Python Pizza Deliveries!")
# # size = input("What size pizza do you want? S, M, or L ")
# # add_pepperoni = input("Do you want pepperoni? Y or N ")
# # extra_cheese = input("Do you want extra cheese? Y or N ")
# # # 🚨 Don't change the code above 👆

# # # Write your code below this line 👇
# # Final_bill = 0
# # if size == "S":
# #     Final_bill += 15
# #     if add_pepperoni == "Y":
# #         Final_bill += 2
# # elif size == "M":
# #     Final_bill += 20
# #     if add_pepperoni == "Y":
# #         Final_bill += 3
# # else:
# #     Final_bill += 25
# #     if add_pepperoni == "Y":
# #         Final_bill += 3
# # if extra_cheese == "Y":
# #     Final_bill += 1

# # print(f"Your final bill is: ${Final_bill}.")

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# # Write your code below this line
# sum_name = (name1 + name2).lower()
# true_count, love_count = 0, 0
# true_count += sum_name.count("t") + sum_name.count("r") + \
#     sum_name.count("u") + sum_name.count("e")

# love_count += sum_name.count("l") + sum_name.count("o") + \
#     sum_name.count("v") + sum_name.count("e")

# score = int(str(true_count)  + str(love_count))

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score > 40 and score < 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
