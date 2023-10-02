import base64

choice = input('''Enter you choice:
1. Encode
2. Decode
=> ''')
def encrypt_pass(password):
        encoded_byte = base64.b64encode(password.encode())
        print(f"The encoded Base64 is {encoded_byte}")
if choice == '1': 
    user_pass = input("Enter your pass to encode it = ")
    encrypt_pass(user_pass)
else:    
    def decrypt_pass(password):
        decode_bytes=base64.b64decode(password)
        decode_data = decode_bytes.decode()
        print(f"The password is = {decode_data}")
    encode_string = input("Enter the base64 encoded password = ")
    decrypt_pass(encode_string)
