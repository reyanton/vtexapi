from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


#write_key()

key = load_key()

password = "*-vtex2020-*".encode()

f = Fernet(key)
encrypted_pass = f.encrypt(password)

print(encrypted_pass)

decrypted_encrypted = f.decrypt(encrypted_pass)
print(decrypted_encrypted)