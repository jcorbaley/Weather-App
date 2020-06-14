#Name: Jason Corbaley
#Datae: 08/07/2019
#Course: DSC 510
#Description: This program will act as a weather app.
#Usage: This program will prompt the user to enter Yes or No on whether or not they would like to see what the weather is
# 		in a city or zip code. If you input y then the program will ask you to enter a city or zip code of your wish.
#		If you enter a valid city or zip code then the program will display the current weather of the location.
#		If you enter an invalid city or zip code you will be prompted to re-enter your location.


import requests

print('Welcome to the weather app!\n')

while True:

	answer = input('Would you like to enter a city or zip code? (Y or N) ')

	if answer == 'Y' or answer == 'y':

		def weather_data(query):

			res = requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=120801c816319a3a0627c0529b85bad8&units=imperial');

			return res.json();

		def print_weather(result,location):

			print("{}'s Weather is:\n".format(location.title()))

			print("Temperature: {}°F ".format(result['main']['temp']))

			print("Wind Speed: {} mph".format(result['wind']['speed']))

			print("Description: {}".format(result['weather'][0]['description']).title())

			print("Weather: {}".format(result['weather'][0]['main']))

		def main():

			location = input('\nEnter the City or Zip Code:')

			print()

			try:

			  query='q='+location;

			  w_data=weather_data(query);

			  print_weather(w_data, location)

			  print()

			except:

			  print('City or Zip Code not found...\n')

		if __name__=='__main__':

			main()

		continue

	elif answer == 'N' or answer == 'n':

		break

	else:

		print('\nAnswer not valid, please try again.\n')

		continue