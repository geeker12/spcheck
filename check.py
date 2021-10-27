import json

with open('sample4.json', 'r') as json_file:
  for field in json_file:
    print(field["query_name"]+" "+field["txt_text"])
    break
