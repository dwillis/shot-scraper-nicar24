# Using Shot-Scraper to grab data from difficult sites
### NICAR 2024
#### Derek Willis, University of Maryland

You can follow along with this hands-on session using GitHub Codespaces. From this repository, click the "Use This Template" button on the top right and choose "Open in a codespace":

![Open in a codespace](codespaces.png)

This repository demonstrates how to use the Python library shot-scraper to scrape websites that rely on a lot of JavaScript and might seem straightforward to scrape but are not. Websites like [this one](https://gozips.com/sports/womens-basketball/roster):

![Akron Women's Basketball Roster](akron_roster.png)

Using your browser's inspect tool, you can see that the structure looks fairly normal: a lot of <div> tags, and player information is contained in <table> tag. Seems simple, right? Just fire up our friends requests and BeautifulSoup and it should be easy:

>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get("https://gozips.com/sports/womens-basketball/roster")
>>> soup = BeautifulSoup(r.text, "html.parser")
>>> soup.find('table')

>>>

Who are you going to believe, this code or your lying eyes? There is a table on that page, but it is getting loaded _after_ the page loads, which means that requests won't "see" it in the source code. Yes, you could play around with HTML sessions or use selenium to emulate a browser, but that table and its rows are right there. Like they are taunting you.

There's a better way, and that's where [shot-scraper](https://shot-scraper.datasette.io/en/stable/index.html) comes in.

Simon Willison, friend of journalists who need to work with data, built this tool to enable a more automated process for taking screenshots. And it's great for that! Just ask Ben Welsh, who built [news.homepages](https://palewi.re/docs/news-homepages/), which automatically grabs screenshots daily. As a screenshot tool it's powerful and flexible.

But if you're working with websites at all in 2024, that means you're likely working with JavaScript. And that's where shot-scraper really shines, because it can execute JavaScript on remote pages just as if you opened up the console log and started typing.


  
