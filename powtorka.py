import requests as r

url = 'https://zajecia-programowania-xd.pl/flagi'
raw_info = r.get(url)
text = raw_info.text

lines = text.split('</p>')
links = []
for line in lines:

    link = line.replace('<p>', '')
    link = link.replace('- ', '')
    link = link.strip()
    if ' ' in link or '<' in link:
        continue
    links.append(link)

# ZADANIE DOMOWE DODATKOWE:
# Napisz funkcje która zadanej liście zliczy
# Wszystkie elementy które mają '.pl' ale tylko '.pl' a nie 
# np. '.eu.pl', '.site.pl', '.com.pl' < --- tych nie zliczamy.
# Czyli funkcja bierze listę stringów z domenami
# Zlicza same '.pl'
# Zwraca liczbe samych '.pl'

# Możesz użyć poniższego przykładu i wcześniejszych kodów aby rozwiązać zadanie.
