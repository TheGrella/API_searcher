import os
from os import listdir
from os.path import isfile, join, isdir
from unittest import skip
from git import Repo
import csv
import shutil

i=1

file = open('Final_API.csv')
csvreader = csv.reader(file)
for row in csvreader:
    if i <= 158:
        print(i)
        skip
    else:
        git_url = f"{row[2]}.git"

        repo_name = "prova"
        Repo.clone_from(git_url, f"./temp_api/{repo_name}")


        mypath = "./temp_api"
        onlydir = [f for f in listdir(mypath) if isdir(join(mypath, f))]
        onlyfile = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for direct in onlydir:
            tree = os.walk(f"{mypath}/{direct}")
            isOpenApi = False
            isGradle = False
            for folder in tree:
                
                if "openapi" in folder[0]:
                    isOpenApi = True

                if "gradle" in folder[0]:
                    isGradle = True

                for dir in folder[1]:
                    if "openapi" in dir:
                        isOpenApi = True

                    if "gradle" in dir:
                        isGradle = True

                for file in folder[2]:
                    if "openapi" in file:
                        isOpenApi = True
                    
                    if "gradle" in file:
                        isGradle = True

        if isOpenApi:
            if isGradle:
                print(f"Repo {i}: {row[1]} Gradle & OpenAPi")

                with open('GradleAndOpen.csv', 'a', encoding='UTF8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([git_url])
            else:
                print(f"Repo {i}: {row[1]} Only OpenAPi")
                with open('OnlyOpenApi.csv', 'a', encoding='UTF8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([git_url])
        else:
            if isGradle:
                print(f"Repo {i}: {row[1]} Only Gradle")
                with open('OnlyGradle.csv', 'a', encoding='UTF8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([git_url])
            else:
                print(f"Repo {i}: {row[1]} Nothing")
        shutil.rmtree(f"{mypath}/{repo_name}")
    i+=1