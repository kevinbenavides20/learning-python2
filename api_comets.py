    
'''
Script description: Get all data about comets
'''
import os
import requests	
	
os.system('clear')


def get_comets():
		global count
		print("::: COMETS INFORMATION :::")
		url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
		
		try:
		
			response = requests.get(url)
			response.raise_for_status()

			data = response.json()
			print(data["bodies"])

			count = 0

			Total = int(input('cantidad de datos a mostrar: '))
			planet = input('Escribe el planeta a buscar: ')
			for comet in data ["bodies"]:

				#if comet['isPlanet'] == True:
				if comet ['englishName'] == planet:
					print('englishName: ', comet['englishName'])
					print('Moons: ', comet['moons'])
					print('Gravity: ', comet['gravity'])
					print('Is planet?: ', comet['isPlanet'])
					print('\n')

					count = count + 1 

				if count == Total:
					break
			print (count)
		except requests.exceptions.RequestException as e:
			print(f'Error: {e}')

get_comets()
print('Total datos', count)