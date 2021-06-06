
import requests
from bs4 import BeautifulSoup
from prac import create_category_folder
from detail_page import extract_img_info as extract_product_info

url = "https://marketb.kr/"
DataBASE = []
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

def extract_product_url(URL,category_title):
    category_name = f"{category_title}"
    create_category_folder(category_name)
    r = requests.get(URL,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    prdLists = soup.find("ul",{"class":"prdList column4"}).find_all("li",{"class":"item"})[:30]
    for prd in prdLists:
        link = prd.find("div",{"class":"box"}).find("div",{"class":"thumbnail"}).find("a")["href"]
        product_info_result = extract_product_info(f'{url}{link}&sort_method=6#Product_ListMenu',category_name)
    return product_info_result
    
       

def extract_max_page(URL):
    r = requests.get(URL,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    pages = soup.find("div",{"class":"xans-product-normalpaging"}).find("ol").find_all("li")
    max_page = int(pages[-1].text.strip("\n").strip(""))
    return 1

def extract_marketb(URL):
    categories = soup.find("nav",{"id":"topMenu"}).find("ul",{"class":"topMenuLi_ul"}).find_all("li",{"class":"topMenuLi"})[2:9]
    for category in categories:
        category_URL = url+category.find("a",{"class":"menuLink"})["href"]
        extract_max_page_result = extract_max_page(category_URL)
        category_title = category.find("a",{"class":"menuLink"}).text
        for page in range(extract_max_page_result):
            URL = f"{category_URL}&page={page}"
            product_result =  extract_product_url(URL,category_title)
            DataBASE.append({category_title:product_result})
    return DataBASE

extract_marketb(url)  

            
            
                    

            
                    