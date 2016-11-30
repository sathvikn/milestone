import requests
from CurrentLocation import get_current_location
headers = {'Authorization' : "Bearer EEQYq44chnPYd1GcTAaL9dkbTrq2Dg4hgZrOV6ddlKCpesirGDZifOkVQ1g4nlnU_lS0n3NRjh_0TYKC-tOpk3HfjPsEBoirvHpwYBL-ydRHced3Kcy9HtdEaasnWHYx"}


def get_possible_destinations(destination_type = 'tourist attractions', city = None, budget = None):

	"""
	Can input a specific location as the DESTINATION_TYPE if looking for a specific type of locations.
	CITY is a string and is used if you want locations in a destination city instead of near you.
	BUDGET is a list of integers 1 to 4 (ex. [1], [1,2,3]).

	The output will be a dictionary. The keys are urls for each of the destinations selected, and the values are dictionaries with the keys listed below:
	dict_keys(['url', 'distance', 'is_closed', 'price', 'name', 'phone', 'image_url', 'categories', 'coordinates', 'id', 'review_count', 'location', 'rating'])


	DO NOT USE BUDGET EXCEPT FOR FOOD ---- THE RETURNED VALUES WILL NOT BE AS GOOD IF YOU DO
	"""

	data = {'term': destination_type, 'open_now': True}


	if city == None:
		latitude, longitude = get_current_location()
		#latitude, longitude = 37.7749, -122.4194
		data['latitude'] = latitude
		data['longitude'] = longitude
	else:
		data['location'] = city

	if budget:
		budget = str(budget)[1:-1]
		data['price'] = budget


	r = requests.get('https://api.yelp.com/v3/businesses/search', headers = headers, params = data)
	response = r.json()
	businesses = response['businesses']

	return dict(zip([biz['url'] for biz in businesses], businesses))

def get_food_destinations(food_type = 'food', budget = None):
	"""
	FOOD_TYPE takes in a string for the type of food place you want ('snacks', 'restaurant', 'vegetarian restaurant', 'thai food' , etc).
	BUDGET is a list of integers 1 to 4 (ex. [1], [1,2,3]).

	The output will be a dictionary. The keys are the names of each of the destinations selected, and the values are dictionaries with the keys listed below:
	dict_keys(['url', 'distance', 'is_closed', 'price', 'name', 'phone', 'image_url', 'categories', 'coordinates', 'id', 'review_count', 'location', 'rating'])
	"""

	locs = get_possible_destinations(destination_type = food_type, budget = budget)
	biz_dicts = locs.values()
	biz_names = [biz['name'] for biz in biz_dicts]
	return dict(zip( biz_names, biz_dicts))



