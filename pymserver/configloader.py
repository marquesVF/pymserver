# -*- coding: utf-8 -*-
from os.path import expanduser, isfile
from ConfigParser import SafeConfigParser


def loadConfiguration():
    home = expanduser("~")
    configuration_file_path = home+"/.pymserver"
    parser = SafeConfigParser()
    config = dict()

    if not isfile(configuration_file_path):
        # Create a new configuration file with default values
        config = open(configuration_file_path, 'w')
        parser.add_section('server')
        parser.set('server', 'port', '3333')
        parser.set('server', 'output_path', home+"/pymserver")
        parser.write(config)
        config['server'] = dict()
        config['server']['port'] = '3333'
        config['server']['port'] = home+"/pymserver"
    else:
        parser.read(configuration_file_path)
        config = dict()
        config['server'] = dict()
        config['server']['port'] = parser.get('server', 'port')
        config['server']['output_path'] = parser.get('server', 'output_path')
    return config

