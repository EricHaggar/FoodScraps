from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *

def findURL(query):

    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 

    # to search 
    found = ""
    for url in search(query, tld = "ca", lang = 'en', num = 2, stop = 1, pause = 1): 
        found = url

    return found


def scrape(url,name):

    revenueScore = 0
    sizeScore = 0
    ratingScore = 0    
    
    # setting first url
    driver = webdriver.Chrome()
    # logging in
    driver.get("https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK")
    # entering username/password
    username = driver.find_element_by_name("username")
    username.send_keys("amham077@uottawa.ca")
    password = driver.find_element_by_name("password")
    password.send_keys("FoodScraps")
    driver.find_element_by_xpath("//*[@class='gd-btn gd-btn-1 fill']").click()
    
    
    try:
        # go to first link
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
        if (ratings == "5"):
            ratingScore = 10
        elif ("4" <= ratings <= "5"):
            ratingScore = 8
        elif ("3" <= ratings < "4"):
            ratingScore = 6
        elif ("2" <= ratings < "3"):
            ratingScore = 4
        elif ("1" <= ratings < "2"):
            ratingScore = 2
        else:
            ratingScore = 5
            
        size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span').text
        if (size == "1 to 50 employees"):
            sizeScore = 2
        elif (size == "51 to 200 employees"):
            sizeScore = 4
        elif (size == "201 to 500 employees"):
            sizeScore = 6
        elif (size == "501 to 1000 employees"):
            sizeScore = 8
        elif (size == "1001 to 10000 employees"):
            sizeScore = 9
        elif (size == "10000+ employees"):
            sizeScore = 10
        else: sizeScore = 5
    
        revenue = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[7]/span').text
        if ("Unknown" in revenue):
            revenueScore = 2
        elif ("million" in revenue):
            revenueScore = 8
        elif ("billion" in revenue):
            revenueScore = 10
        else: revenueScore = 5

    except NoSuchElementException:
        print("finished")

    driver.quit()
    
    return ratingScore, sizeScore, revenueScore


        

        
    
    

    


    
    
    


