import json
jsondata = '{"name":"alice", "age":"20", "country": "USA"}'

jsonvalue = json.loads(jsondata)
print(jsonvalue["name"])