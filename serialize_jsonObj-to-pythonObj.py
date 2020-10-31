#!/usr/bin/python3.8


# Process JSON data returned from a server

# TODO: use the JSON module

import json

def main():

# define a string of some JSON formatted data. We are going to 1st parse this
# json data into a pyton object. Next we'll access some of the data in that
# object. Since we already have the data in a string we'll use the load s 
# function. 
     
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

# TODO: parse the JSON data using load s

    data = json.loads(jsonStr) #This builds a native python dictionary for me.
# Once we have this object we can then work with it like any other pyton 
# dictionary.

    

# TODO: print information from the data structure

# First we'll print out the sandwich name and we can index it by the key name
# which is sandwich.

    print ("Sandwich: " + data['sandwich'])
    if (data['toasted']):
        print("And it's toasted!")
    for topping in data ['toppings']:
#Note, toppings above is an array of toppings. So we can iterate over
#the list.

        print ("Topping: " + topping)

if __name__ == "__main__":
    main()

