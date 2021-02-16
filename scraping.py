import requests
from bs4 import BeautifulSoup
import pprint

#request url of webpage which you want to webscraping
#i used page 1 and page of the wabpage of hacker newsx
#use beautiful soup  and gove html parser
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')


#select link of href in page 1 and page2
#select subtext of two page
link = soup.select('.storylink')
subtext = soup.select('.subtext')
link2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')


#give var maega _link and add two lonk
#give var mega_subtext and add two subtext
mega_links = link + link2
mega_subtext = subtext + subtext2

#vote fun sorted page usin vote arrangement
def sort_story_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'],reverse=True)

#create custom link
#i use two if stattament  ist used len(vote) and 2nd to check vote>99
def create_custom_hn(link,subtext):
    hn = []
    for idx, item in enumerate(link):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
           points = int(vote[0].getText().replace(' points',''))
           if points > 99:
              hn.append({'title':title,'link':href, 'votes':points})
    return sort_story_by_votes(hn)

#i used pprint to print my program preety way
pprint.pprint(create_custom_hn(mega_links, mega_subtext))






