from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt
from bs4 import BeautifulSoup



scoreRecall = []
def scraps( companies):
    for i in range(2,len(companies)):
        driver = webdriver.Chrome()
        driver.get("http://www.healthycanadians.gc.ca/recall-alert-rappel-avis/search-recherche/result-resultat?search_text_1=maple%20leaf%20")
        search = driver.find_element_by_id("search_text_1")
        search.send_keys(companies[i])
        driver.find_element_by_id("search_submit").click()

        searchResults = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text

        if (searchResults == '0 items found for ' + companies[i]):
            scoreRecall.append(0)
        else:
            searchResultsString = driver.find_element_by_xpath('//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text
            searchResults = searchResultsString.split(" ", 2)[0]
            
            if (searchResults<12):
                scoreRecall.append(10)
            else:
                scoreRecall.append(((searchResults%3)+1)*2)

                

        driver.quit()

    return scoreRecall



    




 
        
                              
