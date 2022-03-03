#enabling https
import ssl

from matplotlib.pyplot import title
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

#defining a content class
class content():
    
    #function to scrape New york Times articles
    def scrape_NY_times(self,url):
        '''
        takes a url to a new york times article
        returns the title and the body of the article
        '''
        html = urlopen(url)
        bs = BeautifulSoup(html,'html.parser')
        title = bs.h1.text
        lines = bs.find_all('p',{'class':"story-content"})
        body = '\n'.join([line.text for line in lines])
        return title,body

    #function to scrape Brookings articles
    def scrape_Brookings(self,url):
        '''
        takes a url to a brookings article
        returns the title and the body of the article
        '''
        html = urlopen(url)
        bs = BeautifulSoup(html,'html.parser')
        title = bs.h1.text
        body = bs.find("div",{"class","post-body"}).text
        return title,body

times = content()
print(times.scrape_NY_times('https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'))
print(times.scrape_Brookings('https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'))