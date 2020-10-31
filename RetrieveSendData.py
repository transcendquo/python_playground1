#!/usr/bin/python3.8

# using the requests library to access internet data

#import the requests library
import requests




def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: ----------------------")
    print(resData.headers)
    print("\n")

    print("Returned data: ----------------------")
    print(resData.text)
#    print(resData.content)


# TODO: Pass a custom header to the server 

# The below URL just echos back the content of the get request in JSON format.
url = "http://httpbin.org/get"

# For demo purposes we define a dictionary of some arbitrary key-value pairs
# to send along with the request:

headerValues = {
	"User-Agent" : "Joseph Thomas App /1.0.0"
}


result = requests.get(url, headers=headerValues)
printResults(result)


