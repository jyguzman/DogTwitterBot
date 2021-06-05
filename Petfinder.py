from states import states_list
from random import randint
import requests 
from keys_tokens import client_id 
from keys_tokens import client_secret 

class Petfinder:

	def get_access_token(self):
		data = {
			"grant_type":"client_credentials",
			"client_id":client_id,
			"client_secret":client_secret
		}
		response = requests.post(
			"https://api.petfinder.com/v2/oauth2/token", data=data)
		return response.json()["access_token"]

	def get_dogs_list(self):
		url = ('https://api.petfinder.com/v2/animals?type=dog&location=' 
			+  states_list[randint(0, len(states_list) - 1)])
		header = {'Authorization' : 'Bearer ' + self.get_access_token()}
		response = requests.get(url, headers=header)
		return response.json()['animals']
