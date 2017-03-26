#!/usr/bin/env python3

import requests
from lxml import html
from collections import defaultdict

msg = 'http://boards.fool.com/rankings-20mar2017-32643417.aspx'

# print src url
print ('url = ', msg)

r = requests.get(msg)

tree = html.fromstring(r.content)

pre = tree.xpath('//*[@id="message"]/blockquote/pre/text()')

del pre[0]   # remove header line 'Screen 1 2 3 4...'

tickers = defaultdict(int)

#iterate through each screen scoring the tickers
for line in pre:
  cols = line.split()

  screen = cols[0] # get screen name

  #skip short screens
  if screen.startswith('SHORT'):
    print ('skipping screen', screen)
    continue

  del cols[0] #discard the first column which is the screen name

  weight = 1000

  # iterate through the tickers on this screen scoring them
  for ticker in cols:
    ticker = ticker.strip('*')
    score = weight
    weight = weight - 10

    tickers[ticker] += score

# sort on value descending, print keys and score
for w in sorted(tickers, key=tickers.get, reverse=True):
  print (w, tickers[w])
