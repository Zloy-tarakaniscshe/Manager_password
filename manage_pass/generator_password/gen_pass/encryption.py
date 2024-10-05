from string import ascii_letters, digits, punctuation
import random
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)


def generate_encrypt_password(length=25):
    characters = ascii_letters + digits + punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return fernet.encrypt(password.encode())
