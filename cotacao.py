#!/usr/bin/env python3
"""
Autor: Fábio Berbert de Paula <prefeito@fabio.city>
Data : 26/11/2018
"""

import bs4 as bs

import urllib.request

fonte = urllib.request.urlopen('https://dolarhoje.com/').read()

soup = bs.BeautifulSoup(fonte, 'lxml') #pega so o html

dolar = soup.find("input", {"id": "nacional"})

print(dolar.get('value'))
