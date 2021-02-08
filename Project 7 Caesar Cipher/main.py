alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(start_text,shift_amount,cipher_direction):
  final_text = ""
  for c in range(len(start_text)):
    ind = alphabet.index(start_text[c])
    shift = shift_amount
    if cipher_direction=="decode":
      shift *= -1
    shift_ind = (ind + (shift%26))%26
    final_text += alphabet[shift_ind]
  if cipher_direction=="encode":
    print(f"Here's the encoded result : {final_text}")
  else:
    print(f"Here's the decoded result : {final_text}")

keep_running = "yes"
while keep_running=="yes":
  direction  = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
  text = input("Type youur message : \n")
  number = int(input("Type your shift number : \n"))
  cipher(start_text=text,shift_amount=number,cipher_direction=direction)
  keep_running = input("\nIf you want to go again press 'yes' else 'no' : \n")

