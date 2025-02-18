import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '625831351e177df678e3c2d8ab224b2f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "user_login",
    "password": "user_password"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бумба",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "238694",
    "name": "Булька",
    "photo_id": 2
}

body_catch_in_a_pokeball = {
    "pokemon_id": "238694"
}

'''response = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)

print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)

print(response_change.text)

message = response_change.json()['message']
print(message)

response_catch_in_a_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_in_a_pokeball) 
print(response_catch_in_a_pokeball.text)

message = response_create.json()['message']
print(message)


