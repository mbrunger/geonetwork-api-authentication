#Get GeoNetwork XSRF-token and session-ID from cookie and add to headers for authentication

import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('[username]','[password]') #Replace [username] and [password] with your GeoNetwork username and password
session.post('http://localhost:8080/geonetwork/srv/eng/info?type=me')
session.headers.update({'X-XSRF-TOKEN': session.cookies.get('XSRF-TOKEN')})
session.post('http://localhost:8080/geonetwork/j_spring_security_check')

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9",
"reset": "true",
"username": "[username]", #Replace [username] with your GeoNetwork username
"password": "[password]", #Replace [password] with your GeoNetwork password
"havingXlinkOnly": "false",
"Connection": "keep-alive",
"Cookie": "XSRF-TOKEN="+session.cookies.get('XSRF-TOKEN')+"; JSESSIONID="+session.cookies.get('JSESSIONID')+"; serverTime=1657745480260; sessionExpiry=1657745480260",
"X-XSRF-TOKEN": session.cookies.get('XSRF-TOKEN')
    }
payload = {}


#GeoNetwork API request with authentication

url_metadata = "http://localhost:8080/geonetwork/srv/api/0.1/site/index" #This API request resets the index and is used here as an example.

r_metadata = requests.request("PUT", url_metadata, headers=headers, data=payload)
print("Server response: "+ str(r_metadata))
