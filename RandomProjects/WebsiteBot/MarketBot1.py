############################################################################################
## MARKETBOT1 gives the 100 ticker symbols and prices of stocks listed on tradingview.com 
##
## Edition 1.1 - added name of stock as first column in df
##
## @author Piero Orderique
############################################################################################

from selenium import webdriver 
import pandas as pd

#To configure webdriver to use Chrome browser, we have to set the path to chromedriver
driver = webdriver.Chrome("C:\\Users\\fabri\\miniconda3\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
#website that market data will be extracted from 
driver.get("https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/")

names = driver.find_elements_by_class_name("tv-screener__description") 
#I added a . where there were spaces and it worked!
tickers = driver.find_elements_by_class_name("tv-screener__symbol.apply-common-tooltip") 
#had to look at xpath for 2-3 examples and noticed that only thing different was the index in the first "tr[]"
    #So, since it's the same length as tickers, I added their individual x paths one by one
prices = []
for index, ticker in enumerate(tickers):
    xpathName = '//*[@id="js-screener-container"]/div[4]/table/tbody/tr['+str(index+1)+']/td[2]/span'
    prices.append(driver.find_element_by_xpath(xpathName))

#Makes the offical lists containing the text
tickerList = []
priceList = []
nameList = []
for ticker in tickers:
   tickerList.append(ticker.text)
for price in prices:
   priceList.append(price.text)
for name in names:
    nameList.append(name.text)

driver.close() #closes driver once done extracting data

#let's put the market data into a pandas dataframe
df = pd.DataFrame({'Company': nameList,'Ticker Symbol': tickerList,'Last Price': priceList})
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)  #or can save to csv file 