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

# dictionary storing the company name with latitude and longitude respectively
companies = {   
             "McCain Foods": [46.839, -119.175],
             "Cara Operations": [43.819450, -79.542839],
             "Nature's Path": [43.130, -88.199], 
             "Purity Factories":[40.201020, -82.338220],
             "Saputo": [46.373749, -75.981689],
             "Agropur": [45.494420, -75.477290],
             "Première Moisson": [45.382940, -74.013040],
             "Dan-D Foods": [49.124540, -123.096650],
             "Maple Leaf Foods": [49.866210, -97.162820],
             "Kraft Heinz": [43.758650, -79.347050], 
             "M&M Food Market": [43.596790, -79.747520],
             "PepsiCo": [45.414730, -75.636860],
             "Dare Foods": [43.431160 , -80.448200],
             "Flowers Foods": [30.810660, -83.936910],
             "Pinnacle Foods": [39.864120, -74.996780], 
             "Reser's Fine Foods": [39.036290, -95.633230], 
             "Kawartha Dairy Company": [44.381720, -79.705170],
             "Nestle": [43.760830, -79.412170],
             "Saputo Inc": [46.373749 , -75.981689], 
             "Just Us!": [45.105130, -64.293470],
             "Laura Secord Chocolates": [46.816650 , -71.273610],
             "Voortman Cookies": [43.380540, -79.776040], 
             "Earth's Own Food Company": [49.279200, -123.116220],
             "Canyon Creek Food Company": [53.490280, -113.457390],
             "Chapman's": [44.316750, -80.645560]
             }

# Defining score lists
overallScore = [] 
glassdoorScores = []
recallScores = []
index = 0

for key in companies:
    url = glassdoor_script.findURL(key + '" glassdoor.ca/Overview"')
    glassdoorScores.append(glassdoor_script.scrape(url,key))
    recallScores.append(recalls_script.scrape(key))
    overallScore.append((recallScores[index]*0.7 + glassdoorScores[index][0]*0.3)*10)

    data = {"latitude": companies[key][0], "longitude": companies[key][1], "reviewScore": glassdoorScores[index][0], "sizeScore": glassdoorScores[index][1], "revenueScore": glassdoorScores[index][2], "recallScore": recallScores[index], "overallScore": overallScore[index] }
    database.child("companies").child(key).remove()
    database.child("companies").child(key).set(data)

    index += 1 
    

 