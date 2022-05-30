import json
import urllib.request
with urllib.request.urlopen(
        "http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1131200.json"
) as url:
    json = json.loads(url.read().decode())
    data = json['data'][0]
    tMinima = data['tMin']
    tMaxima = data['tMax']
    print("-------------------------------")
    print("|       Cidade do Porto       |")
    print("-------------------------------")
    print("| Temperatura Mínima: " + tMinima + " ºC |")
    print("| Temperatura Máxima: " + tMaxima + " ºC |")
    print("-------------------------------")