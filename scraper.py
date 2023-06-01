from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []
def scrape():
    for i in range(0,14):
        soup = BeautifulSoup(browser.page_source,"html.parser")

        for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
            
                if index ==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            planets_data.append(temp_list)
            print(temp_list)
    print(planets_data[1])
       
# Calling Method    
scrape()

# Define Header
headers = ["name","mass","radius","distance"]

planets_df = pd.DataFrame(planets_data,columns=headers)

planets_df.to_csv("Scraped_data.csv",index=True,index_label="id")

