import json

# Save heroes to JSON
def save_game(heroes, filename="savefile.json"):
    data = []
    for hero in heroes:
        data.append({
            "name": hero.name,
            "age": hero.age,
            "abilities": hero.abilities,
            "combat": hero.combat,
            "vigor": hero.vigor,
            "mobility": hero.mobility,
            "charisma": hero.charisma,
            "intellect": hero.intellect
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Load heroes from JSON
def load_game(filename="savefile.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        heroes = []
        for h in data:
            hero = Hero(h["name"], h["age"], h["abilities"])
            hero.combat = h["combat"]
            hero.vigor = h["vigor"]
            hero.mobility = h["mobility"]
            hero.charisma = h["charisma"]
            hero.intellect = h["intellect"]
            heroes.append(hero)
        return heroes
    except FileNotFoundError:
        return None
