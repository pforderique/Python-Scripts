##################################################################
## MARKETBOT prints out current market data for selected stocks ##
##################################################################

from selenium import webdriver 
from bs4 import BeautifulSoup 

#To configure webdriver to use Chrome browser, we have to set the path to chromedriver
    #PATH to installed driver: "C:\\Users\\fabri\\miniconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe"
driver = webdriver.Chrome("C:\\Users\\fabri\\miniconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver.get("https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser") #we are parsing with html parser

#get the price of one share of AMZN
#value = soup.find('bg_quote',attrs={'class':"IsqQVc NprOob"})
value = soup.find_element_by_xpath("""<a class="tv-screener__symbol apply-common-tooltip" href="https://www.tradingview.com/symbols/NASDAQ-MSFT/">MSFT</a>""")
print(value.text)