with open("./Input/Names/invited_names.txt") as names:
    lines = names.readlines()

list_of_names = []

for name in lines:
    list_of_names.append(name.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for name in list_of_names:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as to_send:
            to_send.write(letter.replace("[name]", name))

