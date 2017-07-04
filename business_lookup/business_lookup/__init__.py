import os


VERSION_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    'VERSION')


with open(VERSION_FILE_PATH) as f:
    __version__ = f.read().rstrip()


PREFIX = 'business_lookup'
