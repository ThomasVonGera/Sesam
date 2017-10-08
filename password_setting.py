from datetime import datetime
import getpass
import string
import re
import binascii
from base64 import b64encode, b64decode
from random import shuffle
from Crypter import Crypter

DEFAULT_CHARACTER_SET_LOWER_CASE = string.ascii_lowercase
DEFAULT_CHARACTER_SET_UPPER_CASE = string.ascii_uppercase
DEFAULT_CHARACTER_SET_DIGITS = string.digits
DEFAULT_CHARACTER_SET_EXTRA = '#!"§$%&/()[]{}=-_+*<>;:.'

class PasswordSetting(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = None
        self.username = None
        self.legacyPassword = None
        self.notes = None
        self.iterations = 4096
        self.salt = Crypter.createSalt()
        self.creationDate = datetime.now()
        self.modificationDate = self.creationDate
        self.extraCharacters = DEFAULT_CHARACTER_SET_EXTRA
        self.template = 'x' * 10
        self.calculate_template(True, True, True, True)
        self.synced = False

    def __str__(self)





