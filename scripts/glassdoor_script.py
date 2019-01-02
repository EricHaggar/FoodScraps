from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt

def findURL(query):

    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
  
        # to search 
      
    for j in search(query, tld="ca", lang='en', num=2, stop=1, pause=1): 
        url = j

    return j


def scrape(url,name):

    ratingWeight = 0.1
    sizeWeight = 0.1
    revenueWeight = 0.1
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
        if (ratings == "N/A"):
            ratingWeight = 0
            ratingScore = 0
        elif (ratings == "5"):
            ratingScore = 0
        elif (ratings == "4"):
            ratingScore = 2
        elif (ratings == "3"):
            ratingScore = 4
        elif (ratings == "2"):
            ratingScore = 6
        elif (ratings == "1"):
            ratingScore = 8
        elif (ratings == "0"):
            ratingScore = 10
            
        size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span').text
        if (size == "1 to 50 employees"):
            sizeScore = 10
        elif(size == "51 to 200 employees"):
            sizeScore = 8
        elif(size == "201 to 500 employees"):
            sizeScore = 6
        elif(size == "501 to 1000 employees"):
            sizeScore = 4
        elif(size == "10000+ employees"):
            sizeScore = 0
        else: sizeScore = 2
    
        
        revenue = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[7]/span').text
        if (revenue[:6] == "Unknown"):
            revenueScore = 10
        elif(revenue[:11] == "$100 to $500"):
            revenueScore = 6
        elif(revenue[:7] == "$1 to $2"):
            revenueScore = 4
        elif(revenue[:8] == "$5 to $10"):
            revenueScore = 2
        elif(revenue[:11] == "$10+ billion"):
            revenueScore = 0
        else: revenueScore = 8

        overallScore = revenueScore*revenueWeight+sizeScore*sizeWeight+ratingScore*ratingWeight

    except NoSuchElementException:
        print("finished")

    driver.quit()
    
    return overallScore,ratingScore, sizeScore, revenueScore


        

        
    
    

    


    
    
    


