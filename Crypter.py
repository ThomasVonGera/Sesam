from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
import os

class Crypter(object):
    def __init__(self, key_iv):
        if len(key_iv) == 48:
            self.key = key_iv[:32]
            self.iv = key_iv[32:]
        else:
            raise ValueError("Wrong Key_iv length")

    @staticmethod
    def create_key(password, salt, iterations=1024):
        return pbkdf2_hmac(password, salt, iterations)

    @staticmethod
    def createSalt():
        return os.urandom(32)

    @staticmethod
    def add_pkcs7_padding(data):
        length = 16 - (len(data) % 16 )
        data += bytes([length]) * length
        return data

    def encrypt(self, data):
        aes_object = AES.new(self.key, AES.MODE_CBC, self.iv)
        return aes_object.encrypt(self.add_pkcs7_padding(data))

    def encrypt_unpadded(self, data):
        aes_object = AES.new(self.key, AES.MODE_CBC, self.iv)
        return aes_object.encrypt(data)

    @staticmethod
    def remove_pkcs_padding(data):
        return data[:-data[-1]]

    def decrypt(self, encrypt_data):
        aes_object = AES.new(self, AES.MODE_CBC, self.iv)
        return self.remove_pkcs_padding(aes_object.decrypt(encrypt_data))

    def decrypt_unpadded(self, encrypt_data):
        aes_object = AES.new(self, AES.MODE_CBC, self.iv)
        return aes_object.decrypt(encrypt_data)