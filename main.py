from selenium import webdriver
from random import choices
from faker import Faker
from urllib.parse import quote

# declare the link and replace the "viewform" with "FromResponse" to submit it
link = 'https://docs.google.com/forms/d/e/1FAIpQLSeeuouYCKDvMADU40Md0k9nFSiiIe2OwWS8qPPjL1GcCwrRiA/viewform'
link = link.replace('viewform', 'formResponse')

# declare options
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

# decalre the incognitio option and the browser instance
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome(options=option)

for _ in range(10):
    # random choices with different weights
    a = choices(options, [1, 3, 5, 1])[0]
    b = choices(options, [5, 3, 2, 1])[0]
    c = choices(options, [2, 1, 1, 10])[0]
    d = choices(options)[0]
    scale = choices(range(1, 6), [1, 2, 3, 10, 5])[0]
    # random open-ended answers url percent encoded
    longAnswer = quote(Faker().text(), safe='')
    ShortAnswer = quote(Faker().sentence(), safe='')
    # the enteries with answer inside
    entries = f'entry.98489750={a}&entry.1591486926={longAnswer}&entry.231373470={ShortAnswer}&entry.1781145092={b}&entry.1781145092={c}&entry.1761077668={d}&entry.1907356112={scale}'
    # open the browser and reload the tab N number of times (submitting N
    # responses)
    browser.get(f"{link}?{entries}")
