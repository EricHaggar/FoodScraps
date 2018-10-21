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
      
    for j in search(query, tld="com", lang='en', num=1, stop=1, pause=1): 
        url = j

    return j


def scrape(base_url, workbook, name, ss):
    worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
    worksheet.write(0, 1, "Title")
    worksheet.write(0, 2, "Date Written")
    worksheet.write(0, 3, "Rating")
    worksheet.write(0, 4, "Current/Former")
    worksheet.write(0, 5, "Job Title")
    worksheet.write(0, 6, "Location")
    worksheet.write(0, 7, "Recommendation?")
    worksheet.write(0, 8, "Outlook")
    worksheet.write(0, 9, "Main Text")
    worksheet.write(0, 10, "Pros")
    worksheet.write(0, 11, "Cons")
    worksheet.write(0, 12, "Advice to management")
    # setting first url
    url = base_url
    driver = webdriver.Chrome()
    # logging in
    driver.get("https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK")
    # entering username/password
    username = driver.find_element_by_name("username")
    username.send_keys("glassdoorScraper@gmail.com")
    password = driver.find_element_by_name("password")
    password.send_keys("glassdoor")
    driver.find_element_by_xpath("//*[@class='gd-btn gd-btn-1 fill']").click()
    sample_size = ss
    # after login
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
        counter = 0
        loop_count = 0
        sample_size = int(sample_size)
        while loop_count < sample_size/10:
            # search the company
            # ~~~~~~~~~~~~~~~~~~~TITLE OF REVIEW~~~~~~~~~~~~~~~~~~~~~~
            titles = driver.find_elements_by_class_name("reviewLink")
            titlearr = []
            for title in titles:
                counter += 1
                titlearr.append(title.text)

            # ~~~~~~~~~~~~~~~~~~~~TIMESTAMPS~~~~~~~~~~~~~~~~~~~~~~~
            timestamps = driver.find_elements_by_class_name("floatLt")
            datelist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            true_timestamps = []
            for datetime in timestamps:
                if datetime.text[:3] in datelist:
                    true_timestamps.append(datetime.text)
                else:
                    true_timestamps.append("no-date")



            # ~~~~~~~~~~~~~~~~~~~RATINGS~~~~~~~~~~~~~~~~~~~~~~~~~
            ratings = driver.find_elements_by_class_name("value-title")
            ratingarr = []
            for rating in ratings:  # NEED TO REMOVE THE FIRST ONE BECAUSE ITS GETTING OVERALL RATING
                ratingarr.append(rating.get_attribute('title'))
            if int(page) == 1:
                del ratingarr[0]

    
            for index in range(0, len(titlearr)):
                print("INDEX IS: ", index)
                print("ROW: ", int(page)*10+index)
                
                worksheet.write(int(page)*10+index, 3, ratingarr[index])
                loop_count += 1
            try:
                found = driver.find_element_by_css_selector("#FooterPageNav > div > ul > li.page.current.last > span")
                print(found.text)
                workbook.save(name)
                break

            except NoSuchElementException:
                page += 1
                driver.get(basic+str(page)+".htm")
                print("clicked page", str(page))

        workbook.save(name)
        print("done")

    except NoSuchElementException:
        workbook.save(name)
        print("finished")

def mainScraper(a,i):
    company_info = xlwt.Workbook(encoding="utf-8")
    name = "output"+str(i)+".xls"
    sample_size = "10"
    url_link = findURL(a+" glassdoor")
    url_link = url_link[:-4] + "_P1.htm"
    scrape(url_link, company_info, name, sample_size)
    


