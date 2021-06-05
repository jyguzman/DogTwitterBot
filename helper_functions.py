def breed(dog_data):
	return dog_data['breeds']['primary']  + secondary_breed(dog_data)

def secondary_breed(dog_data):
	breed = dog_data['breeds']['secondary']
	isMixed = dog_data['breeds']['mixed']
	if(isMixed == False):
		return ""
	elif (breed == "Mixed Breed" or breed == None): 
		return " mix"
	else:
		return "-" + breed + " mix"

def has_picture(dog_data):
	return (len(dog_data['photos']) != 0)

def is_valid_listing(dog_data): 
	return (dog_data['name'].isalpha() and has_picture(dog_data))

def city_and_state(dog_data):
	return (dog_data['contact']['address']['city'] + ", " +
	dog_data['contact']['address']['state'])

def adoption_link(dog_data):
	return dog_data['url']

def introduce_dog(dog_data):
	return ("This is " + dog_data['name'].title() + ", a " 
				+ dog_data['gender'].lower() + " " + breed(dog_data) +
				" from " + city_and_state(dog_data) + "! Learn more: " +
				adoption_link(dog_data))