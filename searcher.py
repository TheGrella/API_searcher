import csv
import json
from unittest import skip
import requests
import time
import sys

code = 200
last_page = 0
ids = []
if last_page == 0:
  page = 1
else:
  page = last_page
count = 0
index = 0
valid = True
to_append = True
not_appended = 0


headers = {
  'Authorization': 'Token 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'
}


word = sys.argv[1]
counter = sys.argv[2]

print(word)

skip

while code <= 300:
  url = f"https://api.github.com/search/repositories?q={word}&page={page}&per_page=100"
  response = requests.request("GET", url, headers=headers)
  print(response.status_code)
  json_resp = json.loads(response.text)
  
  code = response.status_code
  if(code) == 403:
    code = 200
    page -=1
    print("Dormo per 30 secondi")
    time.sleep(30)
    valid = False
  if(code) == 422:
    print(response.text)
    print("total: "+ str(count + index*10000))
    valid = False

  if valid:
    repos = json_resp["items"]

    for repo in repos:
      count += 1
      if repo["id"] in ids:
        print("ERRRREUEOISNSKLOSSSMSMS    " + str(repo["id"]))
        to_append = False
        not_appended +=1
      else:
        ids.append(repo["id"])

      if (count%10000) == 0:
        count -= 10000
        index += 1

      if to_append:
        with open('./temporanea/Api_total'+str(counter)+'.csv', 'a', encoding='UTF8') as outfile:
          writer = csv.writer(outfile)
          writer.writerow([repo["id"], repo["name"], repo["html_url"]])
      else:
        to_append = True

    print("Repo non appese: "+ str(not_appended))
    print("Page: " + str(page))

  not_appended = 0
  page +=1
  valid = True
code = 200