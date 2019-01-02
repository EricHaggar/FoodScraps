from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt
from bs4 import BeautifulSoup


def scrape(company):
    recallScore = 0
    driver = webdriver.Chrome()
    driver.get(
        "http://www.healthycanadians.gc.ca/recall-alert-rappel-avis/search-recherche/result-resultat?search_text_1=maple%20leaf%20")
    search = driver.find_element_by_id("search_text_1")
    search.send_keys(company)
    driver.find_element_by_id("search_submit").click()

    searchResults = driver.find_element_by_xpath(
    '//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text

    if (searchResults == '0 items found for ' + company):
        recallScore = 0
    else:
        searchResultsString = driver.find_element_by_xpath(
        '//*[@id="search_result_content"]/div[1]/div[2]/div[1]/span').text
        searchResults = int(searchResultsString.split(" ", 2)[0])
        print(searchResults)
        
        if ((searchResults) < 12):
            recallScore = 10
        else:
            recallScore = ((searchResults % 3)+1)*2

    driver.quit()

    return recallScore



    




 
        
                              
