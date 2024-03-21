from geopy.geocoders import Nominatim


def get_lat_long(location):
   
    # calling the Nominatim tool and create Nominatim class
    loc = Nominatim(user_agent="Geopy Library")

    getLoc = loc.geocode(location)

    if getLoc:
        return getLoc.latitude, getLoc.longitude
    else:
        print(f"Failed to retrieve coordinates for location: {location}")
    return None

if __name__ == "__main__": #idiom to determine what script we are in - This essentially allows me to test the script by just running this python file
    location = input("Type a Location as City, State \n")
    coordinates = get_lat_long(location)
    if coordinates:
        print("Latitude:", coordinates[0])
        print("Longitude:", coordinates[1])