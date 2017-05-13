from random import choice

choices = []
print("What to eat today?")

while True:
    choiceIn = raw_input("Enter a restaurant: ")
    if choiceIn == "":
        break
    else:
        choices.append(choiceIn)

print(choice(choices))
