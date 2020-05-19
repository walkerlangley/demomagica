#!/usr/bin/env python
# encoding: utf-8
"""
USSSALoader.py
"""
import os
import re
from urllib.request import urlopen
from zipfile import ZipFile
import csv
import pickle
        
def getNameList():
    if not os.path.exists('./data/ssa_names'):
        print('Directory ./data/ssa_names doesn\'t exist')
        if not os.path.exists('./data/names.zip'):
            print('names.zip does not exist, downloading from catalog.data.gov')
            downloadNames()
        else:
            print('names.zip exists, just unzip')
    
        print('Extracting names from names.zip')
        extractNames()
    return
    
def downloadNames():
    u = urlopen('https://www.ssa.gov/oact/babynames/names.zip')
    localFile = open('./data/names.zip', 'wb')
    print('About to write')
    localFile.write(u.read())
    print('File written')
    localFile.close()
    
def extractNames():
    zf=ZipFile('./data/names.zip', 'r')
    # Extract its contents into <extraction_path>
    # note that extractall will automatically create the path
    zf.extractall(path = './data/ssa_names')
    # close the ZipFile instance
    zf.close()
if __name__ == "__main__":
    getNameList()