import requests

tweet = 'Frozen is a wonderful movie'

data = [
  ('text', tweet),
]
response = requests.post('http://text-processing.com/api/sentiment/', data=data)
data = response.json()
print(data['label'])
