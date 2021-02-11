import pandas

print("NATO Code Words Generator")

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

nato_code_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_code_dict)

user_word = input("Enter a Word : ").upper()
print()

codes = [nato_code_dict[letter] for letter in user_word]

print("Code Words ----------")
print(codes)
