#Libraries 

import urllib
import re
import json
#import requests
from urllib.request import Request
#from requests.auth import HTTPBasicAuth
from datetime import datetime

#variables 

global noofissues,withinaday,withinaweek,morethanaweek
noofissues=0
withinaday=0
withinaweek=0
morethanaweek=0
count=1


print("Sample Input Url Format: https://www.github.com/{username}/{repo}/issues ")
#inputurl="https://github.com/Shippable/support/issues"
inputurl=input('Enter the url link:')

if not inputurl :
    print ("Please enter valid URL")
    exit()

#to get the username and repository name

matchObj = re.match( "https://github.com/(.*)/(.*)/issues" , inputurl)
username=matchObj.group(1)
repo= matchObj.group(2)
print(username)
print(repo)


while True:
    #response = requests.get('https://api.github.com/repos/'+str(username)+'/'+str(repo)+'/issues?state=open&page='+str(count)+'&per_page=100',auth=HTTPBasicAuth('aruntct7', '!amwhat!am007'))
    response = urllib.request.urlopen('https://api.github.com/repos/'+str(username)+'/'+str(repo)+'/issues?state=open&page='+str(count)+'&per_page=500')
    ur = response.read().decode('utf8')
    data=json.loads(ur)
    #data=response.json()

    #to loop through pages
         
    if not data:
        break


        
    count=count+1    

    # to get the current datetime stamp
    date = datetime.now()
    Currentdate=date.strftime('%Y-%m-%d %H:%M:%S')

        
        
    for created_at in data:
        

       
        if len(created_at)== 20 :
            continue


        #to calculate the total number of issues  
        noofissues=noofissues+1 


        #to get the open issues date time    
        openissuedatetime=created_at['created_at']
        
                
        #formatting both current and open issue datetime
        
        d1 = datetime.strptime(Currentdate, "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime(openissuedatetime, "%Y-%m-%dT%H:%M:%SZ")

       
        #finding the difference betwwen the both in seconds
       
        diff= abs((d1 - d2).total_seconds())

        
                
        if  diff <=86400.0:
            
            withinaday=withinaday+1
                    
        if  diff >86400.0 and diff <=604800.0:
            withinaweek=withinaweek+1
                    
        if diff>604800.0:
            morethanaweek=morethanaweek+1
        
         
print ("Result:::")
print ("No of open issues:")
print(noofissues)
print ("No of open issues within 24 hour:")
print(withinaday)
print ("No of open issues within a week:")
print(withinaweek)
print ("No of open issues morethan a week:")
print(morethanaweek)












