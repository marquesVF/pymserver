# -*- coding: utf-8 -*-
from configloader import loadConfiguration
from converter import *
from server import app

def main():
    """

    :return:
    """

    confg = loadConfiguration()
    app.run()
