import requests

data = requests.get("https://www.baidu.com")
print(data.text)


data_post = requests.post("https://www.baidu.com")
print(data_post.text)

