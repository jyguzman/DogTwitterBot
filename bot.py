from Petfinder import Petfinder 
from DogTweeter import DogTweeter
import random

dog_tweets = DogTweeter()
pet_API = Petfinder()

dog_list = pet_API.get_dogs_list()
dog_tweets.tweet_adoption_link(dog_list)
#time.sleep(1000)
dog_tweets.tweet_dog_image()