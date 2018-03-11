# Homework Querying Template Code
#
# This initial helper code will contact the server to request a random address in the United States.
#
# Your goal is to determine most recent bill sponsored by the state senator who represents this address.
# To achieve this goal, you should:
#  - First parse the state's two-letter abbreviation from the address string using regular expressions;
#  - Then use the Census.gov Geocoding API onelineaddress geographies search to find the Upper State Legislative District.
#  - Next use the OpenStates.org API legislator method to determine the full name of the senator in this district.
#  - Finally use the OpenStates.org API bills method to find the title of the last bill sponsored by this senator. (If none, then return 'nothing'.)
#
# Pass your answers to the variables named stateAbbrev, districtNumber, senatorFullName, and sponsoredBillTitle resposectively.
#
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script

##################################################################
### HELPER CODE TO REQUEST RANDOM ADDRESS FROM SERVER
##################################################################
import requests
address=requests.get("https://goo.gl/dyW5Wy").text

##################################################################
### YOUR CODE SHOULD GO BELOW HERE
##################################################################
import re
# import anything else you might need here

import json

email= "jason_webster@brown.edu" #REPLACE THIS

# Frist use reg-ex to find state abbreviation - two capital letters prceeded by comman and trailed by zip
stateAbbrev = re.findall(', ([A-Z]{2,}) [0-9]{5,}', address, re.MULTILINE)[0]

# Second, interact with census.gov API to get upper district number
census_baseurl = "https://geocoding.geo.census.gov/geocoder/"
returntype = "geographies"
searchtype   = "onelineaddress"
param0 = "?address=" + re.sub(' ', '+', address)
param0 = re.sub(',', '%2C', param0)
param1 = "&benchmark=Public_AR_Current"
param2 = "&format=json"
param3 = "&layers=54"
param4 = "&vintage=ACS2017_Current"
census_url = census_baseurl + returntype + "/" + searchtype + param0 + param1 + param2 + param3 + param4
stuff = json.loads(requests.get(census_url).text)
districtNumber = str(int(stuff['result']['addressMatches'][0]['geographies']['2016 State Legislative Districts - Upper'][0]['SLDU']))

# Third, interact with OpenStates API to find the senator for that district
key = '0e21c501-1544-4fd9-941f-2f1d8d9337bd'
openstates_baseurl = 'https://openstates.org/api/v1/'
path_legislator = 'legislators/'
parameter1 = '?apikey=' + key
parameter2 = '&state=' + stateAbbrev
parameter3 = '&district=' + districtNumber
parameter4 = '&chamber=upper'
openstates_url = openstates_baseurl + path_legislator + parameter1 + parameter2 + parameter3 + parameter4
openstates_url
goop = json.loads(requests.get(openstates_url).text)
senatorFullName = goop[0]['full_name']

# Fourth, interact again with OpenStates API to find senator's last bill sponsored
legislator_id = goop[0]['leg_id']
parameter5 = '&sponsor_id=' + legislator_id
parameter6 = '&page=1'
parameter7 = '&sort=created_at'
path_bill = 'bills/'
openstates_url2 = openstates_baseurl + path_bill + parameter1 + parameter5 + parameter6 + parameter7
openstates_url2
junk = json.loads(requests.get(openstates_url2).text)
sponsoredBillTitle = junk[0]['title']

#stateAbbrev='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER
#districtNumber='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER
#senatorFullName='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER
#sponsoredBillTitle='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER

print(stateAbbrev)
print(districtNumber)
print(senatorFullName)
print(sponsoredBillTitle)

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'querying','input':address,'state':stateAbbrev,'district':districtNumber,'senator':senatorFullName,'bill':sponsoredBillTitle}
