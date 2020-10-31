#!/usr/bin/python3.8

# Here we are using POST  to send data to a server using urllib instead of using a GET requst.

# TODO: import the request and parse modules


import urllib.request
import urllib.parse


# TODO: create some data to pass to the POST .
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

url = "http://httpbin.org/post"

data = urllib.parse.urlencode(args)

#defaults to using UTF-8 so no parameters need to be passed

data = data.encode() 

# The below is bad practice because we are setting the parameter name equal to the what the
# variable name is called, but we are passing the data directly to the urlopen function, which 
# tells urllib to automatically switch over to using the POST method behind the scenes without
# having to do anything to explicitly tell urllib to use POST rather than GET.
   
result = urllib.request.urlopen(url, data=data)



# TODO: issue the request with a data parameter to use POST

print("\n Result code: {0}".format(result.status))
print("\n Returned POST data: ----------------------\n")
print(result.read().decode("utf-8"))

# print(result.read())

print ("\nEXPLANATION:\nNotice the arguments in the python dictionary were passed but they are no longer in the args parameter but in the variable called form.")


