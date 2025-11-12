import random
from Heroes import Z_team

class Emergencies:
    def __init__(self, description, req_ability, difficulty):
        self.description = description
        self.req_ability = req_ability
        self.difficulty = difficulty

    def emergency_desk(self):
        print(self.description)

    def user_choice(self):
        choice = int(input("Choose hero number: "))
        selected_hero = Z_team[choice]

        if self.req_ability in selected_hero.abilities:
            print(f"{selected_hero.name} succeeded in handling the emergency!")
        else:
            print(f"{selected_hero.name} struggled with the emergency...")

emergency1 = Emergencies(
    "Today's topic: SDN. Educate the man, prove him wrong!",
    req_ability="intellect",
    difficulty=2
)

emergency2 = Emergencies(
    "Fire in downtown bakery! Rescue civilians.",
    req_ability="combat",
    difficulty=3
)

emergency3 = Emergencies(
    "A villain is causing chaos at the city park! Stop them before civilians get hurt.",
    req_ability="mobility",
    difficulty=2
)

emergency4 = Emergencies(
    "A celebrity is trapped in a dangerous situation. Calm them down and guide them to safety.",
    req_ability="charisma",
    difficulty=3
)

emergency5 = Emergencies(
    "A cyber-attack is spreading through the city's systems. Solve the problem quickly!",
    req_ability="intellect",
    difficulty=4
)

emergency6 = Emergencies(
    "A raging fire blocks the main street. Extinguish it and save trapped citizens!",
    req_ability="combat",
    difficulty=3
)

# Add all emergencies to a list
emergencies = [emergency1, emergency2, emergency3, emergency4, emergency5, emergency6]

def play_shift():
    available_heroes = Z_team.copy()
    current_emergency = random.choice(emergencies)
    current_emergency.emergency_desk()

    for i, hero in enumerate(available_heroes):
        print(i, hero.name)

    choice = int(input("Choose hero number: "))
    selected_hero = available_heroes.pop(choice)

    if current_emergency.req_ability in selected_hero.abilities:
        print(f"{selected_hero.name} succeeded in handling the emergency!")
    else:
        print(f"{selected_hero.name} struggled with the emergency...")

# Loop through multiple shifts
for shift_number in range(3):
    print(f"\n--- Shift {shift_number + 1} ---")
    play_shift()

    
    def level_up():
        print("\nShift completed! Time to level up a hero.")
    
    # Show heroes
    for i, hero in enumerate(Z_team):
        print(f"{i}: {hero.name}")
    
    # Pick a hero
    hero_choice = int(input("Choose a hero to level up: "))
    hero = Z_team[hero_choice]
    
    # Show attributes
    attributes = ["combat", "vigor", "mobility", "charisma", "intellect"]
    for i, attr in enumerate(attributes):
        print(f"{i}: {attr} ({getattr(hero, attr)})")
    
    # Pick an attribute
    attr_choice = int(input("Choose an attribute to increase: "))
    selected_attr = attributes[attr_choice]
    
    # Increase it
    setattr(hero, selected_attr, getattr(hero, selected_attr) + 1)
    print(f"{hero.name}'s {selected_attr} increased by 1!")

    for shift_number in range(3):
        print(f"\n--- Shift {shift_number + 1} ---")
        play_shift()
        level_up()

    def play_shift():
        available_heroes = Z_team.copy()  # fresh list at start of shift
        num_emergencies = 3  # number of emergencies per shift

        for i in range(num_emergencies):
            print(f"\n--- Emergency {i+1} ---")
            current_emergency = random.choice(emergencies)
            current_emergency.emergency_desk()

        # Show available heroes
            for j, hero in enumerate(available_heroes):
                print(j, hero.name)

        # Player chooses a hero
            choice = int(input("Choose hero number: "))
            selected_hero = available_heroes[choice]

        # Check success/failure
            if current_emergency.req_ability in selected_hero.abilities:
                print(f"{selected_hero.name} succeeded in handling the emergency!")
            else:
                print(f"{selected_hero.name} struggled with the emergency...")

    # Shift completed, give level-up
        print("\n--- Shift completed! Time for a level-up! ---")
    # Show heroes
        for j, hero in enumerate(Z_team):
            print(j, hero.name)
        hero_choice = int(input("Choose a hero to level up: "))
        hero_to_upgrade = Z_team[hero_choice]

    # Choose attribute
        attributes = ["combat", "vigor", "mobility", "charisma", "intellect"]
        for k, attr in enumerate(attributes):
            print(k, attr)
        attr_choice = int(input("Choose an attribute to increase: "))
        chosen_attr = attributes[attr_choice]

    # Increase attribute
        setattr(hero_to_upgrade, chosen_attr, getattr(hero_to_upgrade, chosen_attr) + 1)
        print(f"{hero_to_upgrade.name}'s {chosen_attr} increased by 1!")

if __name__ == "__main__":
    for shift_number in range(3):
        print(f"\n--- Shift {shift_number + 1} ---")
        play_shift()

