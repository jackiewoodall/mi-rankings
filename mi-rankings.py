#!/usr/bin/env python

import requests
from lxml import html
from collections import defaultdict

msg = 'http://boards.fool.com/rankings-10oct2016-32428992.aspx'

r = requests.get(msg)

tree = html.fromstring(r.content)

pre = tree.xpath('//*[@id="tdMsg"]/blockquote/pre/text()')

del pre[0]   # remove header line 'Screen 1 2 3 4...'

tickers = defaultdict(int)

#iterate through each screen scoring the tickers
for line in pre:
  cols = line.split()

  screen = cols[0] #discard the first column which is the screen name
  del cols[0]

  weight = 1000

  # iterate through the tickers on this screen scoring them
  for ticker in cols:
    ticker = ticker.strip('*')
    score = weight
    weight = weight - 10

    tickers[ticker] += score


# print src url
print 'url = ', msg

# sort on value descending, print keys and score
for w in sorted(tickers, key=tickers.get, reverse=True):
  print w, tickers[w]
