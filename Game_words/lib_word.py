import json
import requests
import lxml
from bs4 import BeautifulSoup
from urllib.parse import quote
from tqdm import tqdm

data = {}
alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
for i in tqdm(alf):
    url = f"https://kupidonia.ru/spisok/spisok-suschestvitelnyh-russkogo-jazyka/bukva/{quote(i)}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("div",class_='position_title')
    for word in aa:
        if i not in data:
            data[i] = []

        else:
            data[i].append(word.text.split()[0])



with open("lib_word.json",'w',encoding="utf-8") as file:
    json.dump(data,file, ensure_ascii=False)


