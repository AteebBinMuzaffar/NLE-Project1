
# Install beautifulsoup before running the following code

# pip install beautifulsoup4

"""
# **Overview**
Aforementioned are the specifics that the answer encompasses.

### Currencies

*   Dollar Symbol - $
*   Euro Symbol - €
*   Pound Sterling Symbol – £

### Primary Denomination of Currencies
Primary denominations accepted are as follows:

*   Cent Symbol - cent, cents, c, or ¢
*   Pennies Symbol - penny, pennies, or p

### Post-Fix
The following post fixes can be recognized by the script:

*   *Thousands* (**Symbol**: 'K' or 'k' or 'thousand' or 'thousands')
*   *Millions* (**Symbol**: 'm' or 'millions' or 'millions')
*   *Billions* (**Symbol**: 'bn' or 'billion' or 'billions')
*   *Trillions* (**Symbol**: 'tn' or 'trillion' or 'trillions')

### Post-Fixes of Currencies Recognized
The following currency in words can be recognized by the program (case in-sensitive):

*   Dollar
*   Euro
*   Pound

"""

import re
regexForWordsAndSymbols = "[$€£]{1} ?[0-9]+[,]?[0-9]+([.][0-9]+)? ?(k|K|thousand|thousands|million|millions|mn|billion|billions|bn|trillion|trillions|tn)?"
regexForPrimaryDenominations = "[0-9]+[.]? ?(Cent|Cents|cent|cents|c|¢|Penny|penny|Pennies|pennies|p){ |.}"
regexForCurrencyInWords = "[0-9]+ ?(k|K|thousand|thousands|million|millions|mn|billion|billions|bn|trillion|trillions|tn)? ?(Dollar|Dollars|dollar|dollars|Euro|Euros|euro|euros|Pound|Pounds|pound|pounds)"

regex = [regexForWordsAndSymbols, regexForPrimaryDenominations, regexForCurrencyInWords]

def findMoneyInWords(text):
  for expression in regex:
    result = re.search(expression, text)
    if result:
      print(result.group(0))
      return result.group(0)

# HTML to Text conversion script taken from https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
# Install beautifulsoup before running the following code

# pip install beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTextFromHTML(url):
  html = urlopen(url).read()
  soup = BeautifulSoup(html, features="html.parser")
  # kill all script and style elements
  for script in soup(["script", "style"]):
      script.extract()    # rip it out
  # get text
  text = soup.get_text()
  # break into lines and remove leading and trailing space on each
  lines = (line.strip() for line in text.splitlines())
  # break multi-headlines into a line each
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  # drop blank lines
  text = '\n'.join(chunk for chunk in chunks if chunk)
  return text

def processURLToFindMoneyInWords(url):
  textFromHTML = getTextFromHTML(url)
  fetch_result = re.search(".{10}[0-9].{10}", textFromHTML)
  while fetch_result:
    subString = fetch_result.group(0)
    amountFound = findMoneyInWords(subString)
    if amountFound:
      textFromHTML = textFromHTML.replace(amountFound, '')
    else:
      textFromHTML = textFromHTML.replace(subString, '')
    fetch_result = re.search(".{10}[0-9].{10}", textFromHTML)

processURLToFindMoneyInWords("https://www.bbc.com/news/business-41779341")
