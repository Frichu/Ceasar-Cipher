alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type  'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("tpye your message:\n").lower()

shift = int(input("type the shift number:\n"))
#first create a function  called 'encrypt' that takes the "text" and "shift" as inputs.

#combine the encrypt and decrypt funtions into a single function called ceasar


#if a user type a number that is higher than the alphabet

shift = shift % 26

def ceasar(start_text , shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f" the {cipher_direction}d text is {end_text}")

ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)




#def encrypt(plain_text, shift_amount):
    #create an empty string
#   cipher_text = ""
#  for letter in plain_text:
#     position = alphabet.index(letter)
#        new_position = position + shift_amount
#        new_letter = alphabet[new_position]
#       cipher_text += new_letter
#   print(f"the encoded text is {cipher_text}")
#shift each letter of the text 'backward'

#def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#       position = alphabet.index(letter)
#       new_postion = position - shift_amount
#       plain_text += alphabet[new_postion]
#    print(f"the decode text is {plain_text}")

#check if the user is encrypting or decrypting
#if direction == "encode":
#    encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
#    decrypt(cipher_text=text, shift_amount=shift)









