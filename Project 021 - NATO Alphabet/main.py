import pandas

print("NATO Code Words Generator")

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

nato_code_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_code_dict)


def generate_code_words():
    user_word = input("Enter a Word : ").upper()
    print()

    try:
        codes = [nato_code_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, Only alphabets please")
        generate_code_words()
    else:
        print("Code Words ----------")
        print(codes)


generate_code_words()
