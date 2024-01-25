#API:   aplication programing intterface
#Nasa API: https://api.nasa.gov/ Get commets
#API_KEY_NASA: mGxpWzmD8QniR6OrPCOyU5szMmI7XNMHmER9xIH1
#developer: Kevin Benavides
#Date: 24012024
#https://api.nasa.gov/neo/rest/v1/neo/3726712api_key=mGxpWzmD8QniR6OrPCOyU5szMmI7XNMHmER9xIH1
import requests 


def get_commet_data(api_key):
    print(':: COMMET INFORMATION ::')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/3726712api_key={api_key}'

    try:
        #realizar la solicitud a la Api
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()

        print(datos)
    except requests.exceptions.RequestException as e:
        print(f'error al realizar la peticion de la nasa {e}')


API_KEY_NASA = 'mGxpWzmD8QniR6OrPCOyU5szMmI7XNMHmER9xIH1'
get_commet_data(API_KEY_NASA)

