import requests
import json
import pandas as pd
import time

URL = "https://api.raydium.io/pools"

cookies = {
  'privacy-policy': '1,XXXXXXXXXXXXXXXXXXXXXX'
}

page = requests.get(URL)

html = page.text
res1 = json.loads(html)
active = []

for i in res1:
  if i['apy'] is not None:
    active.append(i)

print(active)
# starttime = time.time()
# while True:
#   page = requests.get(URL)
#   html = page.text
#   res2 = json.loads(html)
#   if res2[2] != res1[2]:
#     print(f'{(time.time()-starttime)/60} minutes since last change')
#     print(res2[2])
#   res1 = res2
#   time.sleep(3600 - ((time.time() - starttime) % 3600))

# df = pd.DataFrame(columns=['pool', 'apy', 'tvl', ])
# for i in res:

# soup = BeautifulSoup(html, "html.parser")

# for child in soup.find("div").children:
#   if child.name == 'span':
#      data_content = json.loads(child.text)
#      print(data_content["ou"])
