from bs4 import BeautifulSoup
import requests

def atrodi_virsrakstu(url):
  r = requests.get(url)
  html = r.text
  soup = BeautifulSoup(html, "html.parser")
  virsraksti = []
  for h1 in soup.find_all("h1"):
    virsraksts = h1.text
    virsraksti.append(virsraksts)
  return virsraksti

url = input("Ievadi URl:")
virsraksti = atrodi_virsrakstu(url)
print(virsraksti)
  