import os
import glassdoor_script
import recalls_script

overalScore=[]

scores=glassdoor_script.main()

numOfRecalls,secoreRecall=recalls_script.b()

for i in range(0,len(numOfRecalls)):
        
    overalScore[i]=(secoreRecall[i]*0.7+scores[i]*0.3)/100
    





