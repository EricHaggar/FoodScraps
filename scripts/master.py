import glassdoor_script
import recalls_script

aymen = []


companies = ['"McCain Foods"', '"Cara Operations"', '"'+"Nature's Path"+'"', '"Purity Factories"', '"Saputo"', '"Sobeys"', '"Agropur"', '"Première Moisson"', '"Bothwell Cheese"', '"Dan-D Foods"', '"Maple Leaf Foods"', '"Kraft Heinz"', '"M&M Food Market"',
             '"PepsiCo"', '"Dare Foods"', '"Flowers Foods"', '"Pinnacle Foods"', '"'+"Reser's Fine Foods"+'"', '"Kawartha Dairy Company"', '"Nestle"', '"Saputo Inc"', "Just Us!",
             '"Laura Secord Chocolates"', '"Voortman Cookies"', '"'+"Lester's Foods Ltd."+'"', '"'+"Earth's Own Food Company"+'"', '"Canyon Creek Food Company"', "Cara Operations",
             '"'+"Chapman's"+'"', '"Metro Inc."']

overallScore = [] 
glassdoorScores = []
recallScores = []


for i in range(0,len(companies)):
    url = glassdoor_script.findURL(companies[i]+'" glassdoor.ca/Overview"')
    glassdoorScores.append(glassdoor_script.scrape(url,companies[i]))
    recallScores.append(recalls_script.scrape(companies[i]))
    overallScore.append((recallScores[i]*0.7 + glassdoorScores[i][0]*0.3)*10)
    print(overallScore)

    





