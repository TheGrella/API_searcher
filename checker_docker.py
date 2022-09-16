import os
from os import listdir
from os.path import isfile, join, isdir
from unittest import skip
from git import Repo
import csv
import shutil

i=1

file = open('OnlyOpenApi.csv')
csvreader = csv.reader(file)
for row in csvreader:
    git_url = f"{row[0]}"

    repo_name = "prova"
    Repo.clone_from(git_url, f"./temp_api/{repo_name}")


    mypath = "./temp_api"
    onlydir = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    onlyfile = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for direct in onlydir:
        tree = os.walk(f"{mypath}/{direct}")
        isDocker = False

        for folder in tree:
            
            if "docker" in folder[0]:
                isDocker = True

            for dir in folder[1]:
                if "docker" in dir:
                    isDocker = True

            for file in folder[2]:
                if "docker" in file:
                    isDocker = True
       
        if isDocker:
            print(f"Repo {i}: Docker & OpenAPi")
            with open('OpenApi&Docker.csv', 'a', encoding='UTF8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([git_url])
        else:
            print(f"Repo {i}: Only OpenAPi")
            with open('OpenApiOnly.csv', 'a', encoding='UTF8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([git_url])
    shutil.rmtree(f"{mypath}/{repo_name}")
    i+=1