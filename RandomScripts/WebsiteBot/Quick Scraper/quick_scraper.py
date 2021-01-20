'''
Quick Web Scraper

Piero Orderique
20 Jan 2021

Quick Web Scraper returns a list of everything on a website
that is associated with an id or class. Very simple and 
straight forward program for the "quick webscraper" who 
just wants a list of all Xs included on one site.
'''
from bs4 import BeautifulSoup 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # forget about updating my guy

# personal interests : in my case, I want a list of all OOD methods listed on a site
WEBSITE = "https://refactoring.guru/design-patterns/cpp"
design_methods = []

# create web driver and navigate to website you need
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(WEBSITE)
content = driver.page_source

# the parser checks for the html within specified class
soup = BeautifulSoup(content, features="html.parser")

for obj in soup.find_all(attrs={'class':"dp-pattern-title"}):
    design_methods.append(obj.text)
    # print(a.text)

driver.quit()
print(design_methods)