# Using Shot-Scraper to grab data from difficult sites
### NICAR 2024
#### Derek Willis, University of Maryland

This repository demonstrates how to use the Python library shot-scraper to scrape websites that rely on a lot of JavaScript and might seem straightforward to scrape but are not. Websites like [this one](https://byucougars.com/sports/womens-basketball/roster/season/2023-2024/):

![BYU Women's Basketball Roster](byu_roster.png)

Using your browser's inspect tool, you can see that the structure looks normal: a lot of <div> tags, and player information is contained in a `roster-card-item` div. Seems simple, right? Just fire up 


You can follow along with this hands-on  
