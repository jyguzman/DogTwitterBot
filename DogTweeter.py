import tweepy
import requests
import os
import random
import keys_tokens as k_t
import helper_functions as helpers
from dog_puns import puns

class DogTweeter:

	def __init__(self):
		self.api = self.get_twitter_API(k_t.API_key, k_t.API_secret_key)

	def get_twitter_API(self, API_key, API_secret_key):
		auth = tweepy.OAuthHandler(API_key, API_secret_key)
		auth.set_access_token(k_t.access_token, k_t.access_secret_token)
		return tweepy.API(auth)

	def tweet_adoption_link(self, dog_list):
		if (len(dog_list) > 0): 
			dog = dog_list[random.randint(0, len(dog_list) - 1)]
			if (helpers.is_valid_listing(dog)):
				self.api.update_status(helpers.introduce_dog(dog)) 
				print("Adoption link tweeted.")
			else: self.tweet_dog_image()
		else: self.tweet_dog_image()

	def tweet_dog_image(self):
		dog_api_response = requests.get("https://dog.ceo/api/breeds/image/random")
		img_url = dog_api_response.json()['message']	
		img_response = requests.get(img_url)	
		dog_image = "dog.jpg"
		with open(dog_image, "wb") as img:
			for chunk in img_response:
				img.write(chunk)
		
		pun = puns[random.randint(0, len(puns) - 1)]
		self.api.update_with_media(dog_image, status=pun)
		print("Dog image tweeted.")
		os.remove(dog_image)