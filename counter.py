import os
from os import listdir
from os.path import isfile, join, isdir
from unittest import skip
from git import Repo
import csv
import shutil


mypath = "./openApi_specs"

onlydir = [f for f in listdir(mypath) if isdir(join(mypath, f))]

print(len(onlydir))