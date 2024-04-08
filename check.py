import requests 
import json
url=" http://127.0.0.1:8000"
data=requests.post(url)
jsons=json.dumps(data)
print(jsons)