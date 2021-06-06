import requests
response = requests.get("https://marketb.kr/web/product/small/202103/97e1f68ce5b96145790eda0ea7da7e99.jpg")

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()