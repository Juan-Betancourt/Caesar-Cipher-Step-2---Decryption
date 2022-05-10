alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# if direction == "encode":
#   def encrypt(plain_text, shift_amount):
#       cipher_text = ""
#       for letter in plain_text:
#           position = alphabet.index(letter)
#           new_position = position + shift_amount
#           new_letter = alphabet[new_position]
#           cipher_text += new_letter
#       print(f"The encoded text is {cipher_text}")
#   encrypt(plain_text=text, shift_amount=shift)

# elif direction == "decode":
#   def decrypt(encode_text, shift_number):
#       cipher_text = ""
#       for letter in encode_text:
#           position = alphabet.index(letter)
#           new_position = position - shift_number
#           new_letter = alphabet[new_position]
#           cipher_text += new_letter
#       print(f"The decode text is {cipher_text}")
#   decrypt(encode_text=text, shift_number=shift)

#simplified method utilizing less code
def caesar():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  cipher_text = ""
  for letter in text:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
      else:
        new_position = position - shift  
      new_letter = alphabet[new_position]
      cipher_text += new_letter
  if direction == "encode":
    print(f"The encoded text is {cipher_text}")
  else:
    print(f"The decoded text is {cipher_text}")

caesar()
        
    
