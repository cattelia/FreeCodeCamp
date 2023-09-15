#Service Oriented Approach
'''
Data that is spread out over the internet. Some applications cannot contain everything - like a travel website.
What it does is that it talks to all these locations on the webs for you and congregates it to one place.
'''

#Web Services
'''

'''

#Application Program Interface " API"
'''
Itself is largely abstract in that it specifies an interface and controls the behavior of the objects
specified in that interface. The software that provides the functionality described by an API is said
to be an "implementation" of the API. An API is typically defined in terms of the programming language
used to build the application.

Rate limiting
'''
#Google Maps API http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2c+MI
{
    "status":"OK",
    "results": [
        {
            "geometry": {
                "location_type" : "APPROXIMATE",
                "location" : {
                    "lat" : 42.2808256,
                    "lng" : -83.7430378
                }
            },
            "address_components" : [
                {
                    "long_name" : "Ann Arbor",
                    "type" : [
                        "locality",
                        "political"
                    ],
                    "short_name" : "Ann Arbor"
                }
            ],
            "formatted_address" : "Ann Arbor, MI, USA",
            "types" : [
                    "locality",
                    "political"
            ]
        }
    ]
}

#Can we write a program that reads this json?

import urllib.request, urllib.parse, urllib.error
import json

#base URL
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    #parse.urlencode() takes a key and value, which will pass information to the URL for example:
    # %2C == ,
    # + == " "
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print("Retrieving: {}".format(url))
    uh = urllib.request.urlopen(url)
    data = uh.read().decode() #This is the json file that we are now going to attempt to read.
    print("Retrieved {} characters".format(len(data)))

    try: 
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("=== Failure to Retrieve ===")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    log = js["results"][0]["geometry"]["location"]["lng"]
    print("{} {}".format(lat, log))
    location = js["results"][0]["formatted_address"]
    print(location)

    #APIs protect themselves by keys or signatures. We will be looking at that next.