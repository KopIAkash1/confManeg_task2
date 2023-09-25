import json
import requests

if __name__ == "__main__":
    ## ЭТАП ПОДКЛЮЧЕНИЯ К САЙТУ
    mask = "https://pypi.org/pypi/"
    mask2 = "/json"
    while True:
        libName = input("Enter name of lib -> ")
        url = mask + libName + mask2
        site = requests.get(url=url)
        if(site.status_code == 404):
            print("The library with this name could not be obtained! Enter another name.")
        else:
            break
    ## ЭТАП СОЗДАНИЯ JSON
    jsonFile = json.loads(site.text)
    requiresDist = jsonFile['info']['requires_dist']
    #ФОРМАТИРОВАНИЕ ТЕКСТА В УДОБНЫЙ ФОРМАТ
    for i in range(0,len(requiresDist)):
        requiresDist[i] = str(requiresDist[i]).split('>',1)[0]
    #print(requiresDist)