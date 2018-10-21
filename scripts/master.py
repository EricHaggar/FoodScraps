import os
import glassdoor_script 

companies = ["Neilson", "McCain Foods"]

for i in range(len(companies)):
        glassdoor_script.mainScraper(companies[i], i)


