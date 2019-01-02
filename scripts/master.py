import glassdoor_script
import recalls_script
import pyrebase

# Add firebase connection here!
config = {

    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

companies = ['"McCain Foods"', '"Cara Operations"', '"'+"Nature's Path"+'"', '"Purity Factories"', '"Saputo"', '"Sobeys"', '"Agropur"', '"Première Moisson"', '"Dan-D Foods"', '"Maple Leaf Foods"', '"Kraft Heinz"', '"M&M Food Market"',
             '"PepsiCo"', '"Dare Foods"', '"Flowers Foods"', '"Pinnacle Foods"', '"'+"Reser's Fine Foods"+'"', '"Kawartha Dairy Company"', '"Nestle"', '"Saputo Inc"', "Just Us!",
             '"Laura Secord Chocolates"', '"Voortman Cookies"', '"'+"Earth's Own Food Company"+'"', '"Canyon Creek Food Company"', "Cara Operations",
             '"'+"Chapman's"+'"']           

overallScore = [] 
glassdoorScores = []
recallScores = []


for i in range(0,len(companies)):
    url = glassdoor_script.findURL(companies[i]+'" glassdoor.ca/Overview"')
    glassdoorScores.append(glassdoor_script.scrape(url,companies[i]))
    recallScores.append(recalls_script.scrape(companies[i]))
    overallScore.append((recallScores[i]*0.7 + glassdoorScores[i][0]*0.3)*10)
    latitude = -5 
    longitude = 10
    print(overallScore)

    data = {"latitude": -10, "longitude": 4, "reviewScore": 5, "sizeScore": 6, "revenueScore": 2, "recallScore": 34, "overallScore": 15 }
    database.child("companies").child(companies[i]).remove()
    database.child("companies").child(companies[i]).set(data)






