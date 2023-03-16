# # # # # # # Randomisation!
# # # # # # # 메르센 트위스터! -> 난수 생성 알고리즘
# # # # # # # python random module
# # # # # # import random
# # # # # # Random_int = random.randint(10, 20)  # 10,20 포함

# # # # # # Random_float = random.random()  # 0 ~ 1 까지인데 1은 포함 안함;

# # # # # # love_score = random.radint(0, 100)

# # # # # # Remember to use the random module
# # # # # # Hint: Remember to import the random module here at the top of the file. 🎲

# # # # # # Write the rest of your code below this line 👇

# # # # # import random

# # # # # ht = random.randint(0, 1)

# # # # # if (ht == 0):
# # # # #     print("Heads")
# # # # # else:
# # # # #     print("Tails")

# # # # # List!
# # # # fruits = ["apple", "orange", "strawberry"]

# # # # print(fruits)
# # # # print(fruits[-1])
# # # # fruits.append("melon")
# # # # fruits.extend(["blueberry, grape"])

# # # # Import the random module here
# # # import random
# # # # Split string method

# # # names_string = input("Give me everybody's names, separated by a comma. ")
# # # names = names_string.split(", ")
# # # # 🚨 Don't change the code above 👆

# # # # Write your code below this line 👇

# # # who = random.randint(0, len(names))
# # # print(f"{names[who]} is going to buy the meal today!")
# # a = []
# # b = []
# # c = [a, b]

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# col = int(position[0])
# row = int(position[1])

# map[row - 1][col - 1] = "X"


# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
