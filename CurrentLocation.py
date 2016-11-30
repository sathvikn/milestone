from urllib.request import urlopen
import json

def get_current_location():
    """
    This function takes no arguments and returns a tuple with the user's current location (latitude, longitude)
    """
    f = urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string.decode("utf-8"))
    return(location['latitude'], location['longitude'])
