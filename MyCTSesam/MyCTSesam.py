from preference_manager import PreferenceManager
from base64 import b64decode
import argparse
import getpass
import sys

def create_settings_manager(kgkManager):
    aPreferenceManager = PreferenceManager()
	return PasswordSettingsManager(aPreferenceManager), aPreferenceManager