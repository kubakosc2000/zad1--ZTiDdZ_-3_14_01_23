import base64

def encrypt_base64(text):
    encoded_text = base64.b64encode(text.encode())
    return encoded_text.decode()

def decrypt_base64(text):
    decoded_text = base64.b64decode(text.encode()).decode()
    return decoded_text

# Test
original_text = "Hello World!"
encoded_text = encrypt_base64(original_text)
print("Encoded text:", encoded_text)
decoded_text = decrypt_base64(encoded_text)
print("Decoded text:", decoded_text)
