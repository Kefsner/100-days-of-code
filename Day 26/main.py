import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

word = input("Enter a word: ").upper()

print([nato_dict[letter] for letter in word])
