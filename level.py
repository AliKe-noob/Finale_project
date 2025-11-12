import json
import random

# ---- JSON Save/Load ----
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

# ---- Automatic Play ----
class Level:
    def __init__(self, name, introduction, emergencies):
        self.name = name
        self.introduction = introduction
        self.emergencies = emergencies

    def intro_to_game(self):
        print(f"\n{self.name}\n{self.introduction}")

    def play(self, heroes):
        print(f"\nStarting {self.name}...\n")
        for emergency in self.emergencies:
            # Pick a hero automatically
            suitable_heroes = [h for h in heroes if emergency.req_ability in h.abilities]
            if suitable_heroes:
                chosen_hero = random.choice(suitable_heroes)
                print(f"{chosen_hero.name} handled the emergency: {emergency.description}")
            else:
                chosen_hero = random.choice(heroes)
                print(f"{chosen_hero.name} struggled with: {emergency.description}")

        # Automatically level up a random hero
        hero_to_level = random.choice(heroes)
        attr_to_increase = random.choice(["combat", "vigor", "mobility", "charisma", "intellect"])
        setattr(hero_to_level, attr_to_increase, getattr(hero_to_level, attr_to_increase) + 1)
        print(f"{hero_to_level.name}'s {attr_to_increase} increased by 1!")

        # Save after level
        save_game(heroes)
