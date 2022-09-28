# Zelda

![Scrape all the links](scrapememe.png)

Finding urls for backfills on websites without sitemaps can be a pain. 😣

Scrape all the links on a webpage using Beautiful Soup!

Simply select the appropriate script for your scenario. Then modify the start url and classes according to the comments. Finally save and run it. The urls will print to your terminal.

The first three scenarios are for use with a specific webpage (example: https://website.com/news/world/2022/09/). 

The fourth scenario is for webpages with pagination, such as press release sections and archives with multiple pages and a "Next" button (example: https://website.com/release/2/). *Remember to modify the start and end of the loop.* 

Note: These scripts are fast! No need to make a cup of tea while they run.


## Installation

Install the following libraries:
```
pip install requests
pip install html5lib
pip install bs4
```

    
## Scenarios

* **Scenario 1:** Extract **all** urls in `<a>` tags on a webpage
* **Scenario 2:** Extract urls in `<a>` tags with a specific class on a webpage 
* **Scenario 3:** Extract urls in `<a>` tags, in `<div>` tags with a specific class, on a webpage 
* **Scenario 4:** Extract urls in `<a>` tags, in `<div>` tags with a specific class, on multiple webpages 
