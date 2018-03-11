#Run this script at the end when you are ready to submit your homework to the autograder.

import hw_querying  # imports your hw5 module
import requests

submissionFile=open('hw_querying.py','r')
postData=hw_querying.yourSubmission()


with open('token','a+') as tokenFile:
	token=tokenFile.read();

if len(token)<6: 
	with open('token','w') as tokenFile:
		tokenResponse=requests.post("https://script.google.com/macros/s/AKfycbyBDf_xQftwKphaD4jFJ9hH0SL7JhnM_jyYNeXUuYugLHlhvU8/exec",data={'requestingToken':1,'email':postData["email"]});
		token=tokenResponse.text;
		tokenFile.write(token)

postData["token"]=token
postData["submission"]=submissionFile.read()
subResponse=requests.post("https://script.google.com/macros/s/AKfycbyBDf_xQftwKphaD4jFJ9hH0SL7JhnM_jyYNeXUuYugLHlhvU8/exec",data=postData)
responseFile=open('submissionResponse.txt','wb+')
responseFile.write(subResponse.text.encode('utf8'))
print(subResponse.text)
