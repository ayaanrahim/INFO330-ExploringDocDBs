from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data4']
pikachu = pokemonColl.find_one({"name": "Pikachu"})
attack = pokemonColl.find({"attack": {"$gt": 150}})
attack2 = []
for a in attack:
    attack2.append(a)
ability = pokemonColl.find({"abilities": {"$in": ["Overgrow"]}})
ability2 = []
for a in ability:
    ability2.append(a)
print(len(attack2))
