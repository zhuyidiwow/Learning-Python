from random import choice

choices = []
choices.append("wan")
choices.append("chao")
choices.append("nian")
choices.append("wan")
choices.append("wan")
print("Who should buy waimai today?")

while True:
    choiceIn = raw_input("Enter a person: ")
    if choiceIn == "":
        break
    else:
        choices.append(choiceIn)

print(choice(choices))
