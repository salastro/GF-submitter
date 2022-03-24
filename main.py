from selenium import webdriver
from random import choices, randint
from faker import Faker
from urllib.parse import quote

# declare the link and replace the "viewform" with "FromResponse" to submit it
link = 'https://docs.google.com/forms/d/e/1FAIpQLSeeuouYCKDvMADU40Md0k9nFSiiIe2OwWS8qPPjL1GcCwrRiA/viewform'
link = link.replace('viewform', 'formResponse')

# declare form options
formOptions = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

# decalre the incognitio option and the browser instance
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome(options=option)

for _ in range(10):

    # random choices with different weights
    a = choices(formOptions, [1, 3, 5, 1])[0]
    b = choices(formOptions, [5, 3, 2, 1])[0]
    scale = choices(range(1, 6), [1, 2, 3, 10, 5])[0]

    # random open-ended answers url percent encoded
    longAnswer = quote(Faker().text(), safe='')
    ShortAnswer = quote(Faker().sentence(), safe='')

    # the enteries with answer inside
    entries = f'entry.98489750={a}&entry.1591486926={longAnswer}&entry.231373470={ShortAnswer}&entry.1761077668={b}&entry.1907356112={scale}'

    # add a random number of mutliple options
    # TODO: improve implementation: mutliple options having the same option is
    # still a posssibility this way, and this does not play well in producing
    # statsitcally suffecient results. It's only advanatage, however, is the
    # more organic look of the data.
    # If this does not appeal to you then modifty the code to reproduce the old
    # behaviour of a fixed number of options with a statsitcally suffiecent
    # results and a less bit organic data
    for _ in range(randint(1, len(formOptions) + 1)):
        entries += f'&entry.1781145092={choices(formOptions, [7, 3, 4, 2])[0]}'

    # open the browser and reload the tab N number of times (submitting N
    # responses)
    browser.get(f"{link}?{entries}")
