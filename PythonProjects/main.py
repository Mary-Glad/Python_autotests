import requests
import json

token = 'b1289268043c7a4736261d7a1e362262'

response_auth = requests.post('https://pokemonbattle.me:5000/trainers/reg', headers = {'Content-Type' : 'application/json'},
json = {
     "trainer_token": token,
    "email": "puchka333@yandex.ru",
    "password": "Puchok123"
    })

print(response_auth.text)

response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email', headers = {'Content-Type' : 'application/json'},
json = {
     "trainer_token": token
    })

print(response_confirm.text)

response_create = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json',
'trainer_token' : token},
json = {
    "name": "Dipsy",
    "photo": "https://dolnikov.ru/pokemons/albums/07.png"
})

print(response_create.text)

pokemon_id = response_create.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json',
'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Kooky",
    "photo": "https://dolnikov.ru/pokemons/albums/07.png"
})

print(response_change.text)

response_catch = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json',
'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id
})

print(response_catch.text)