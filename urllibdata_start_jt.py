#!/usr/bin/python3.8

# This simple python script wll use urllib to go to a test web page and print out the returned result code, data headers, and the returned XML data both in raw binary and UTF-8 format.



# using urllib to request data

# TODO: import the urllib request class

import urllib.request
    
# the URL to retrieve our sample data from 
url = "http://httpbin.org/xml"

# TODO: open the URL and retrieve some data

result = urllib.request.urlopen(url)
# TODO: Print the result code from the request, should be 200 OK

print("Return code: {}\n".format(result.status))

# TODO: print the returned data headers

print("Headers: ----------------------\n")
print(result.getheaders())   

print ("\n")

# TODO: print the returned data itself

print ("XML Raw Bytes below: --------------------:\n")
print(result.read()) 

print ("\n")

result = urllib.request.urlopen(url)
print ("XML UTF-8 formatted output below:-------------------:\n")
print (result.read().decode('utf-8'))
    
