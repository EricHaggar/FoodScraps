from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt
import json

companies = ['"McCain Foods"', "Cara Operations", "Nature's Path", "Olymel", "Purity Factories", "Rogers Sugar", "Saputo", "Naya Waters", "Sobeys", "Daiya", "SunOpta",
             "Organic Meadow Cooperative", "Agropur", "Première Moisson", "Bothwell Cheese", "Dan-D Foods", "Maple Leaf Foods", "Kraft Heinz", "M&M Food Market",
             "PepsiCo", "Dare Foods", "Flowers Foods", "Pinnacle Foods", "Reser's Fine Foods", "Kawartha Dairy Company", "Nestle", "Saputo Inc", "Just Us!",
             "Laura Secord Chocolates", "Voortman Cookies", "Lester's Foods Ltd.", "Earth's Own Food Company", "Canyon Creek Food Company", "Cara Operations",
             "Chapman's", "Metro Inc."]



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
    ratingWeight=0.1
    sizeWeight=0.1
    revenueWeight=0.1

    
    
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
            ratingWeight=0
            scoreRate=0
        elif (ratings == "5"):
            scoreRate=0
        elif (ratings == "4"):
            scoreRate=2
        elif (ratings == "3"):
            scoreRate=4
        elif (ratings == "2"):
            scoreRate=6
        elif (ratings == "1"):
            scoreRate=8
        elif (ratings == "0"):
            scoreRate=10
            
        print(scoreRate)
        nbr = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span').text
        if (nbr == "1 to 50 employees"):
            scoreSize=10
        elif(nbr == "51 to 200 employees"):
            scoreSize=8
        elif(nbr == "201 to 500 employees"):
            scoreSize=6
        elif(nbr == "501 to 1000 employees"):
            scoreSize=4
        elif(nbr == "10000+ employees"):
            scoreSize=0
        else: scoreSize=2
        

        
        
        print(scoreSize)
        revenue=driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[7]/span').text
        if (revenue[:6] == "Unknown"):
            scoreRevenue=10
        elif(revenue[:11] == "$100 to $500"):
            scoreRevenue=6
        elif(revenue[:7] == "$1 to $2"):
            scoreRevenue=4
        elif(revenue[:8] == "$5 to $10"):
            scoreRevenue=2
        elif(revenue[:11] == "$10+ billion"):
            scoreRevenue=0
        else: scoreRevenue=8
        print(scoreRevenue)
        
        

        x = {
          "name": name,
          "review": ratings,
          "revenue": revenue,
          "size": nbr
        }

        # convert into JSON:
        with open('data.txt', 'w') as outfile:  
            json.dump(x, outfile)
        driver.quit()


        

    except NoSuchElementException:
        print("finished")

def main():
        url=findURL(companies[0]+'" glassdoor.ca/Overview"')
        scrape(url,companies[0])
        

        
    
    

    


    
    
    


