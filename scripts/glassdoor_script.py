from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt

companies = ["Neilson", "McCain Foods"]



def findURL(query):

    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
  
        # to search 
      
    for j in search(query, tld="ca", lang='en', num=2, stop=1, pause=1): 
        url = j

    return j


def scrape():
    
    # setting first url
    url = ""
    driver = webdriver.Chrome()
    # logging in
    driver.get("https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK")
    # entering username/password
    username = driver.find_element_by_name("username")
    username.send_keys("amham077@uottawa.ca")
    password = driver.find_element_by_name("password")
    password.send_keys("FoodScraps")
    driver.find_element_by_xpath("//*[@class='gd-btn gd-btn-1 fill']").click()
    
    for i in range(len(companies)):
        try:
            # go to first link
            url=findURL(companies[i]+" glassdoor.ca/Overview")
            print(url)
            driver.get(url)
            url_arr = url.split("_")
            basic = url_arr[0]+"_P"
            page_arr = list(url_arr[1])
            page = ""
            for char in page_arr:
                if char.isdigit():
                    page += char
            # this is the current page we are on
            page = int(page)
            ratings = driver.find_element_by_class_name("ratingNum").text
            print(ratings)

        

        except NoSuchElementException:
            workbook.save(name)
            print("finished")
    

    
def mainScraper():
    for i in range(len(companies)):
        company_info = xlwt.Workbook(encoding="utf-8")
        name = "output"+str(i)+".xls"
        sample_size = "20"
        url_link = findURL(companies[i]+" glassdoor.ca/Overview")
        print (url_link)
        scrape(url_link, company_info, name)

    
    
    


