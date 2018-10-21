import os
import glassdoor_script
import recalls_script

overalScore=[]
numOfRecalls,secoreRecall=recalls_script.b()
scores=glassdoor_script.main()
for i in range(0,4):
    overalScore[i]=(secoreRecall[i]*0.7+scores[i]*0.3)/100





