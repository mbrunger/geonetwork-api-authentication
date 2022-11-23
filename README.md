# geonetwork-api-authentication
GeoNetwork API authentication script in python

### GeoNetwork API authentication
GeoNetwork is a metadata catalog webapplication. The application can also be accessed with an API. The API uses a security filter to prevent CSRF attacks. Authentication of API requests works with a token that is stored in a cookie. The GeoNetwork manual describes the authentication procedure [here](https://geonetwork-opensource.org/manuals/3.10.x/en/customizing-application/misc.html#example-of-csrf-call-using-curl) using curl. However, the manual does not give an example of an authentication method using python.

### Authentication with python
This python script can be used for the authentication of the GeoNetwork API. The script takes the XSRF-token and the session-ID from the cookie and adds it to the headers. The script contains the index reset API-function as an example of an API request. The script has been developed using GeoNetwork version 3.10.6 and is based on the standard authentication method in GeoNetwork (user/password stored in database).
