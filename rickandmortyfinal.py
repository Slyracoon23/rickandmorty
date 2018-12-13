import requests
import json

base_url="https://rickandmortyapi.com/api/"
character_url=base_url+"character/"
location_url=base_url+"location/"
episode_url=base_url+"episode/"

class Base():
	def api_info(self):
		return requests.get(base_url).json()

	def schema(self):
		temp=requests.get(character_url).json()
                return temp['info'].keys()


class Character():

	def get_all(self):
		return requests.get(character_url).json()

	def get_page(self,number):
		return requests.get(character_url+'?page='+str(number)).json()

	def get(self,id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(character_url+str(id)).json()

	def filter(self,**kwargs):
		for value in kwargs:
				kwargs[value]=value+"="+kwargs[value]
		query_url='&'.join([values for values in kwargs.values()])
		final_url=character_url+"?"+query_url
		return requests.get(final_url).json()

	def schema(self):
		temp=requests.get(character_url).json()
		return temp['results'][0].keys()

class Location():

	def get_all(self):
		return requests.get(location_url).json()

	def get(self,id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(location_url+str(id)).json()

	def filter(self,**kwargs):
		for value in kwargs:
				kwargs[value]=value+"="+kwargs[value]
		query_url='&'.join([values for values in kwargs.values()])
		final_url=location_url+'?'+query_url
		return requests.get(final_url).json()

	def schema(self):
		temp=requests.get(location_url).json()
		return temp['results'][0].keys()


class Episode():

	def get_all(self):
		return requests.get(episode_url).json()

	def get(self,id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(episode_url+str(id)).json()

	def filter(self,**kwargs):
		for value in kwargs:
				kwargs[value]=value+"="+kwargs[value]
		query_url='&'.join([values for values in kwargs.values()])
		final_url=episode_url+'?'+query_url
		return requests.get(final_url).json()

	def schema(self):
		temp=requests.get(episode_url).json()
		return temp['results'][0].keys()

if __name__ == '__main__':
    char = Character()
    loc = Location()
    epi = Episode()


    # Give the user some context.
    print("\nWelcome to the rickandmortyapi center. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
    choice = ''

# Start a loop that runs until the user enters the value for 'quit'.

    while choice != 'q':
    # Give all the choices in a series of print statements.
        print("\n[1] Enter 1 to get all characters.")
        print("[2] Enter 2  to get an id character.")
        print("[q] Enter q to quit.")

    # Ask for the user's choice.
        choice = raw_input("What would you like to do? ")

    # Respond to the user's choice.
        if choice == '1':
            print json.dumps(char.get_all(), indent=4)
        elif choice == '2':
            id = input("\nINPUT ID ")
            print json.dumps(char.get(id), indent=4)
        elif choice == 'q':
            print("\nThanks for playing. See you later.\n")
        else:
            print("\nI don't understand that choice, please try again.\n")

# Print a message that we are all finished.
    print("Thanks again, bye now.")

        #print json.dumps(char.get(2), indent=4)
