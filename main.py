from selenium import webdriver
from random import choices
from faker import Faker
from urllib.parse import quote

link = 'https://docs.google.com/forms/d/e/1FAIpQLSeeuouYCKDvMADU40Md0k9nFSiiIe2OwWS8qPPjL1GcCwrRiA/viewform'
link = link.replace('viewform', 'formResponse')
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome(options=option)

for _ in range(10):
    a = choices(options, [1, 3, 5, 1])[0]
    b = choices(options, [5, 3, 2, 1])[0]
    c = choices(options, [2, 1, 1, 10])[0]
    d = choices(options)[0]
    scale = choices(range(1, 6), [1, 2, 3, 10, 5])[0]
    longAnswer = quote(Faker().text(), safe='')
    ShortAnswer = quote(Faker().sentence(), safe='')
    entries = f'entry.98489750={a}&entry.1591486926={longAnswer}&entry.231373470={ShortAnswer}&entry.1781145092={b}&entry.1781145092={c}&entry.1761077668={d}&entry.1907356112={scale}'
    browser.get(f"{link}?{entries}")
