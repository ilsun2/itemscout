import requests
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
def download_image(list,path):
    for url in list:
        name = url.split("/")[-1]
        response = requests.get(url,headers=headers)
        with open(f"{path}/{name}", "wb") as file:
            file.write(response.content)
        file.close()
    return