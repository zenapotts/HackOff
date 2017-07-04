import os
from ConfigParser import ConfigParser


def read_config(config_file='./development.ini'):
    if 'BUSINESS_LOOKUP_SETTINGS' in os.environ:
        config_file = os.environ['BUSINESS_LOOKUP_SETTINGS']

    conf = {}
    config = ConfigParser()
    # Don't lowercase keynames
    config.optionxform = str
    found = config.read(config_file)
    
    if (config_file not in found):
        raise Exception(
            "Tried to read config file at %s but it was not found"
            % config_file)

    for section in config.sections():
        conf[section] = dict(config.items(section))
    for key, value in config.items('sqlalchemy'):
        conf['SQLALCHEMY_%s' % key.upper()] = value
    return conf
