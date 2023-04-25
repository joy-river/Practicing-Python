
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import string

with open("invited_names.txt") as inv:
    temp = inv.read()
    inv_list = temp.split("\n")


with open("starting_letter.txt") as start:
    template = start.read()


for i in inv_list:
    with open(f"../MailMerge/ReadyToSend/{i}.txt", mode="w") as file:
        file.write(template.replace("[name]", i))


# readlines -> 여러 줄을 리스트로 반환해줌
# strip -> 앞 뒤 공백을 없애줌

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp