import json
import requests

data = {
    "User": {
        "name":"Reason Regmi",
        "age": 24,
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

json_str = json.dumps(data, indent=4)
print(json_str)





