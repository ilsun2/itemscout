import requests
import csv
from bs4 import BeautifulSoup
from prac import create_product_folder
from save_imgage import download_image
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
fieldnames = ['title', 'origin', 'price', 'shipping', 'main_img', 'detail_img',"옵션 없음"]
product_list = []
def extract_img_info(URL,category_title):
    global extract_img_result
    category_name = f"{category_title}"
    r = requests.get(URL,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    infoAreas = soup.find("table",{"id":"JProductInfo"})
    
    if(infoAreas == None):   
        print("XXXX")
    else:
        infoAreas = infoAreas.find_all("tr",{"class":"xans-record-"})
        exel_title = infoAreas[0].find("td").find("span").text.strip("당일발송")
        title = exel_title.replace("/","-").strip("").replace(" ","_")
        if("시리즈" in title):
            pass
        else:
            ThumbImages = soup.find_all("img",{"class":"ThumbImage"})
            main_img=[]
            for thumbimg in ThumbImages:
                main_img.append("http:"+thumbimg["src"])
            detail_img = []
            details = soup.find("div",{"class":"cont"}).find_all("img")
            for detail in details:
                detail_img.append("http://marketb.kr"+detail["src"])
            origin = infoAreas[2].find("td").find("span").text+"산"
            if(infoAreas[4].find("td").find("span").text == "3%"):
                price = infoAreas[3].find("td").find("span").find("strong",{"id":"span_product_price_text"}).text.strip("원").replace(",","")
            else:
                price = infoAreas[4].find("td").find("span").find("strong",{"id":"span_product_price_text"}).text.strip("원").replace(",","")
            
            options = soup.find("div",{"class":"infoArea"}).find("table",{"class":"xans-product-option"}).find_all("tbody")
            option_name = []
            option_key = "옵션 없음"
    
            if("당일발송" not in options[1].text):
                option_key = options[1].find("tr").find("th").text
                if(option_key not in fieldnames):
                    fieldnames.append(option_key)
                option_selects = options[1].find("tr").find_all("option")[2:]
                for option in option_selects:
                    option_name.append(option.text)
            shipping = infoAreas[-1].find("td").find("span").text
            extract_img_result = {
                "title":exel_title,
                "origin":origin,
                "price":price,
                option_key : option_name,
                "shipping":shipping,
                "main_img":main_img,
                "detail_img":detail_img
            }
            product_folder_path = create_product_folder(category_name,title)
            download_image(main_img,product_folder_path)
            product_list.append(extract_img_result)
            download_image(detail_img,product_folder_path)
    product_csv_file = write_csv(category_name, product_list)
    
    return product_csv_file
    

def write_csv(category_name, list):
    with open(f'{category_name}.csv', mode="w",newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in list :
            writer.writerow(item)
    return csv_file
    

