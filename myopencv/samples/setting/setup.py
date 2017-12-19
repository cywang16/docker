import os

def getSetupDir():
    return os.path.dirname(os.path.realpath(__file__))

def getPicturesDir():
    return '{}/Pictures'.format(getSetupDir())
