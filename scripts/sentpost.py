import requests
import json
test = json.dumps({"key": "value","vgvghvhv": [{"guhi": "jkjhkjh","uhuihuih":"jkjoijo"}],"jkjl": "jkhkj"})
r = requests.post('http://testtest.ml/post/e10415b78ad05b04c695ea239267dd0523afd8b2c713108f84ad446d26208bd5',  data=test)
print(r.text)

# r = requests.get('http://127.0.0.1:5000/get-file')
# print(r.text)
