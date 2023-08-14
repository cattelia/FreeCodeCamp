
#Exercise 1: GeoJSON
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print("Retrieving: {}".format(url))
    uh = urllib.request.urlopen(url)
    data = uh.read().decode() 
    print("Retrieved {} characters".format(len(data)))

    try: 
        js = json.loads(data)
    except:
        js = None


    if not js or "status" not in js or js["status"] != "OK":
        print("=== Failure to Retrieve ===\n")
        print(js["error_message"])
        continue

    print(json.dump(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    log = js["results"][0]["geometry"]["location"]["lng"]
    print("{} {}".format(lat, log))
    location = js["results"][0]["formatted_address"]
    print(location)

    '''
    {
        "error_message" : "You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account",
        "results" : [],
        "status" : "REQUEST_DENIED"
    }
    '''

    '''
        if js["status"] == "REQUEST_DENIED":
        print("You need a key")
        break
    else:  
        if not js or "status" not in js or js["status"] != "OK":
            print("=== Failure to Retrieve ===")
            print(data)
            continue
    '''