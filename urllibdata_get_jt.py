#!/usr/bin/python3.8


# Here we are using a GET request to send data to a server using urllib

# TODO: import the request and parse modules


import urllib.request
import urllib.parse


url = "http://httpbin.org/get"


# TODO: create some data to pass to the GET request.
# First we need to define some parameters. It is very common to have parameters stored in
# a python dictionary object. So we'll create one of those with the arbitrary 
# name    args   below:


args = {

	"name": "Joseph Thomas",
	"is_author": True
}


# Before we can send the above parameters to the server they must be put in a format that
# can be passed as part of a URL.

# So to do that we must encode the parameters using the parse module that was imported at
# the top of this script.

# Next we will need to call the (URL encode) method below on the parameter dictionary that 
# was created in  args above:

# TODO: the data needs to be url-encoded before passing as arguments
# The name    data    is arbitrary and could be called anything.


data = urllib.parse.urlencode(args)


# TODO: issue the request with the data params as part of the URL
# We already have the request which is going to the URL.  We just need to add the query string to the URL that is now
# being represented by this data. Remember that in a typical URL string, the query data gets appended after a question mark on the URL
# so the below ? is simply appended.  Everything after the .urlopen below is the   query   argument that ulib.parse.urlencode expects.  


result = urllib.request.urlopen(url + "?" + data)

# TODO: issue the request with a data parameter to use POST


   
print("Result code: {0}".format(result.status))
print("Returned data: ----------------------\n")
print(result.read().decode("utf-8"))


