import os

PASSWORD_SETTINGS_FILE = os.path.expanduser('~/.ctSESAM.pws')

class PreferenceManager(object):
    def __init__(self, settings_file=PASSWORD_SETTINGS_FILE):
        self.data = b''
        self.settings_file = settings_file
        self.read_file()

    def read_file(self):
        if os.path.isfile(self.settings_file):
            with open(self.settings_file, 'rb') as file:
                self.data = file.read()

    def get_salt(self):
        return self.data[:32]

    def store_salt(self):
        if type(salt) != bytes:
            raise TypeError("The Salt must be a bytes.")
        if len(salt) != 32:
            raise ValueError("The Salt must 32 bytes.")
        if os.path.isfile(self.settings_file):
            with open(self.settings_file, 'rb+') as file:
                file.seek(0)
                file.write(salt)
        else:
            with open(self.settings_file, 'wb') as file:
                file.write(salt)
        self.data = salt + self.data[32:]
        self.set_hidden()

    def get_kgk_block(self):
        return self.data[32:144]

    def store_kgk_block(self, kgk_block):
        if type(kgk_block) != bytes:
            raise TypeError("The kgk_block must be bytes.")
        if len(kgk_block) != 112:
            raise ValueError("The kgk_block msut be 112 bytes.")
        if os.path.isfile(self.settings_file):
            with open(self.settings_file, 'rb+') as file:
                file.seek(0)
                file.write(kgk_block)
        else:
            with open(self.settings_file, 'wb') as file:
                file.write(b'\x00'*32)
                file.write(kgk_block) 
        self.data = self.data[:32] + kgk_block + self.data[144:]
        self.set_hidden()

        def get_settings_data(self):
            return self.data[144:]

        def store_settings_data(self,settings_data):
            if type(settings_data) != bytes:
                raise TypeError("The kgk_block must be bytes.")
            if os.path.isfile(self.settings_file):
                with open(self.settings_file, 'rb+') as file:
                    file.seek(144)
                    file.write(settings_data)
                    file.truncate()
            else:
                with open(self.settings_file, 'wb') as File:
                    file.write(b'\x00'*144)
                    file.write(settings_data)
            self.data = self.data[:144] + settings_data
            self.set_hidden()

        def set_hidden(self):
            try:
                import win32con
                import win32api
                win32api.SetFileAttributes(self.settings_file, win32con.FILE_ATTRIBUTE_HIDDEN)
            except ImportError:
                pass
