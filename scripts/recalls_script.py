from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt
from bs4 import BeautifulSoup



companies = ['"McCain Foods"', "Cara Operations", "Nature's Path", "Olymel", "Purity Factories", "Rogers Sugar", "Saputo", "Naya Waters", "Sobeys", "Daiya", "SunOpta",
             "Organic Meadow Cooperative", "Agropur", "Première Moisson", "Bothwell Cheese", "Dan-D Foods", "Maple Leaf Foods", "Kraft Heinz", "M&M Food Market",
             "PepsiCo", "Dare Foods", "Flowers Foods", "Pinnacle Foods", "Reser's Fine Foods", "Kawartha Dairy Company", "Nestle", "Saputo Inc", "Just Us!",
             "Laura Secord Chocolates", "Voortman Cookies", "Lester's Foods Ltd.", "Earth's Own Food Company", "Canyon Creek Food Company", "Cara Operations",
             "Chapman's", "Metro Inc."]

numOfRecalls = []
secoreRecall = []
def b():
    for i in range(0,len(companies)):
        driver = webdriver.Chrome()
        driver.get("http://www.healthycanadians.gc.ca/recall-alert-rappel-avis/search-recherche/result-resultat?search_text_1=maple%20leaf%20")
        search = driver.find_element_by_id("search_text_1")
        search.send_keys(companies[i])
        driver.find_element_by_id("search_submit").click()

        searchResults = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text

        if (searchResults == '0 items found for ' + companies[i]):
            numOfRecalls.append(0)
            secoreRecall.append(0)
        else:
            searchResults = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text[0]
            numOfRecalls.append(int(searchResults))
            if (0<int(searchResults)<=2):
                secoreRecall.append(2)
            elif (2<int(searchResults)<=5):
                secoreRecall.append(4)
            elif (5<int(searchResults)<=8):
                secoreRecall.append(6)
            elif (8<int(searchResults)<=12):
                secoreRecall.append(8)
            else: secoreRecall.append(10)
        print(searchResults)
        driver.quit()
    return numOfRecalls,secoreRecall



    




 
        
                              
