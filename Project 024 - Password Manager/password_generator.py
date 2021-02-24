
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generate(nr_letters=6, nr_symbols=2, nr_numbers=2):
    l_letters = [random.choice(letters) for _ in range(0, nr_letters)]
    l_numbers = [random.choice(numbers) for _ in range(0, nr_numbers)]
    l_symbols = [random.choice(symbols) for _ in range(0, nr_symbols)]

    password_list = l_letters + l_numbers + l_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password
