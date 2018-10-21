from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt
from bs4 import BeautifulSoup



companies = ["McCain Foods", "Cara Operations", "Nature's Path", "Olymel", "Purity Factories", "Rogers Sugar", "Saputo", "Naya Waters", "Sobeys", "Daiya", "SunOpta",
             "Organic Meadow Cooperative", "Agropur", "Première Moisson", "Bothwell Cheese", "Dan-D Foods", "Maple Leaf Foods", "Kraft Heinz", "M&M Food Market",
             "PepsiCo", "Dare Foods", "Flowers Foods", "Pinnacle Foods", "Reser's Fine Foods", "Kawartha Dairy Company", "Nestle", "Saputo Inc", "Just Us!",
             "Laura Secord Chocolates", "Voortman Cookies", "Lester's Foods Ltd.", "Earth's Own Food Company", "Canyon Creek Food Company", "Cara Operations",
             "Chapman's", "Metro Inc."]

numOfRecalls = []

for i in range(0,len(companies)):
    driver = webdriver.Chrome()
    driver.get("http://www.healthycanadians.gc.ca/recall-alert-rappel-avis/search-recherche/result-resultat?search_text_1=maple%20leaf%20")
    search = driver.find_element_by_id("search_text_1")
    search.send_keys("'"+ companies[i]+"'")
    driver.find_element_by_id("search_submit").click()

    searchResults = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text

    if (searchResults == '0 items found for ' + companies[i]):
        numOfRecalls.append(0) 
    else:
        searchResults = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text[0]
        numOfRecalls.append(int(searchResults)) 



 
        
                              
