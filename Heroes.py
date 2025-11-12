import json
from Attributes import Attributes

class Heroes(Attributes):
    def __init__(self, name, age, bio, abilities, combat, vigor, mobility, charisma, intellect):
        super().__init__(combat, vigor, mobility, charisma, intellect)
        self.name = name
        self.age = age
        self.bio = bio
        self.abilities = abilities

    def info(self):
        print(f"""
Hero: {self.name}, Age: {self.age}
BIO: {self.bio}

Attributes:
Combat:    {self.combat}
Vigor:     {self.vigor}
Mobility:  {self.mobility}
Charisma:  {self.charisma}
Intellect: {self.intellect}
Abilities: {self.abilities}
        """)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "bio": self.bio,
            "abilities": self.abilities,
            "combat": self.combat,
            "vigor": self.vigor,
            "mobility": self.mobility,
            "charisma": self.charisma,
            "intellect": self.intellect
        }

    # 🔹 Create hero back from dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["bio"],
            data["abilities"],
            data["combat"],
            data["vigor"],
            data["mobility"],
            data["charisma"],
            data["intellect"]
        )
    
def save_game(filename, heroes):
    data = [hero.to_dict() for hero in heroes]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Game saved successfully!")


def load_game(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        heroes = [Heroes.from_dict(hero_data) for hero_data in data]
        print("Game loaded successfully!")
        return heroes
    except FileNotFoundError:
        print("No save file found. Starting new game.")
        return None


Sonar = Heroes("Viktor",
                 23,
                  "Humanoid Bat, mostly human. Harvard‑educated con artist turned Phoenix Program operative. " \
                  "Charismatic, sometimes morally grey; balancing his past as con‑artist with current hero role.",
                   ["flight"], 
                   1, 
                   1, 
                   2, 
                   3, 
                   4,)

Flambae = Heroes("Chad",
                 27,
                  "Former villain turned hero; pyrokinesis user. " \
                  "Hot‑headed (both literally and figuratively), competitive, has tension with other heroes.",
                   ["flight", "flame"], 
                   3, 
                   2, 
                   2, 
                   1, 
                   1,)

Invisigal = Heroes("Courtney",
                 20,
                  "Snarky, abrasive; often shows attitude and struggle with teamwork. " \
                  "Ex-villain, turned herself in few months ago. ",
                   ["invisibility"], 
                   3, 
                   1, 
                   3, 
                   2, 
                   1,)

Z_team = [Sonar, Flambae, Invisigal]
for hero in Z_team:
    hero.info()