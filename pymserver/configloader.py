# -*- coding: utf-8 -*-
from os.path import expanduser, isfile
from ConfigParser import SafeConfigParser


def loadConfiguration():
    home = expanduser("~")
    configuration_file_path = home+"/.pymserver"
    if not isfile(configuration_file_path):
        makedirs(configuration_file_path)
