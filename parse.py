import scrapy
from os import listdir, getcwd

p = f"{getcwd()}/pages"
l = listdir(p)

def isSolved (document) :
    r = scrapy.Selector(text=document)
    indicators = r.css(f"div.js-accepted-answer-indicator.flex--item.fc-green-700.py6.mtn8")
    rs = [ind for ind in indicators if 'd-none' not in ind.attrib.get('class') and ind.css('div.ta-center') is not None]
    return len(rs) > 0

pages = [page for page in l if isSolved(open(f"{p}/{page}", 'r').read())]
print(f"Pages to follow are : {pages}")