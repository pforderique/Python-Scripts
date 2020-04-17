######################################################
## This is the attempt to read info from a website ##
######################################################

from selenium import webdriver 
from bs4 import BeautifulSoup 
import pandas as pd #I'll use this to store information

#To configure webdriver to use Chrome browser, we have to set the path to chromedriver
    #PATH to installed driver: "C:\\Users\\fabri\\miniconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe"
driver = webdriver.Chrome("C:\\Users\\fabri\\miniconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")

###################################################################################################
### FLIPKART BRANCH INCLUDES THE EXAMPLE OF EXTRACTING MULTIPLE INFO FROM THE FLIPKART WEBSITE  ###
###################################################################################################
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser") #we are parsing with html parser

#This parent class is nested in <a> tag, which holds the <div> in which the other attributes are in.
#Therfore, maybe look for <a> and it will also have an href link maybe?
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):    
    #get class name for each attribute and use code below:
    name = a.find('div', attrs={'class':'_3wU53n'})
    price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class':'hGSR34'})
    #add them to your list
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

#store info in a data frame and save as csv!
df = pd.DataFrame({'Product Name':products,
                   'Price':prices,
                   'Rating':ratings})
df.to_csv("C:\\Users\\fabri\\OneDrive\\Documents\\DasText\\csvFiles\\products.csv", index=False, encoding='utf-8')
