import os
from os import listdir
from os.path import isfile, join, isdir
from unittest import skip
from git import Repo
import csv
import shutil

i=1
a = []
j="Final_API.csv"

file = open(j)
csvreader = csv.reader(file)

repo_save = "prova"
mypath = "./temp_api"
saving_path = "./openApi_specs"


for row in csvreader:
    if i <= 211:
        #print(i)
        skip
    else:
        try:
            #git_url = f"https://TheGrella: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@github.com/{row[2]}.git"
            git_url = f"{row[2]}.git"
            

            local = False
            swagger = False
            
            try:
                Repo.clone_from(git_url, f"./temp_api/{repo_save}")
                
            except:
                skip

            _, owner, repo_name = row[2][8:].split("/")
            print(f"{j}:{owner}_{repo_name}")

            number_file = 0

            onlydir = [f for f in listdir(mypath) if isdir(join(mypath, f))]
            onlyfile = [f for f in listdir(mypath) if isfile(join(mypath, f))]

            for direct in onlydir:
                specs = []
                tree = os.walk(f"{mypath}/{direct}")

                for folder in tree:
                    for file_name in folder[2]:
                        if (".json" in file_name) or (".yaml" in file_name):
                            if(file_name == "package-lock.json" or file_name == "package.json"):
                                skip
                            else:
                                try:
                                    file = open(f"{folder[0]}/{file_name}", "r")
                                    
                                    for line in file:
                                        if "http://localhost:" in line:
                                            local = True
                                        if ("openapi" in line) or ("swagger" in line):
                                            swagger = True

                                    
                                    if local and swagger:
                                        with open('OpenApi.csv', 'a', encoding='UTF8') as outfile:
                                            writer = csv.writer(outfile)
                                            writer.writerow(git_url)
                                        try:
                                            os.makedirs(f"openApi_specs/{repo_name}_{owner}")
                                        except(FileExistsError):
                                            print("1")
                                        number_file +=1
                                        print(f"{j}:{folder[0]}/{file_name}")
                                        shutil.move(f"{folder[0]}/{file_name}", f"./openApi_specs/{repo_name}_{owner}/{str(file_name)}")
                                except(UnicodeDecodeError):
                                    skip

            if local and swagger:
                shutil.move(f"./temp_api/{repo_save}",f"./temp_api/{owner}_{repo_name}")
                shutil.move(f"./temp_api/{owner}_{repo_name}", "./cluster_API")
            else:
                shutil.rmtree(f"{mypath}/{repo_save}")

        except(FileNotFoundError):
            shutil.rmtree(f"{mypath}/{repo_save}")
    i+=1