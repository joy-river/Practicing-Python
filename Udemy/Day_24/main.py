with open("my_file.txt", mode="a") as file:
    #content = file.read()

# file = open("my_file.txt")
#
# cont = file.read()
# print(cont)
#
# file.close()
    file.write("\nNew text")


with open("new_one.txt", mode="w") as newfile:
    newfile.write("New file")

#with open("../Day_1/Udemy_Day_1.py") as root:

with open("../../../../../../mnt/c/", mode="r") as test:
    print(test.read())