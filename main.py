import unittest
from Heroes import Heroes 
from level import load_game
from Emergencies import emergencies 
from save import save_game
import os

class TestHTMS(unittest.TestCase):
    def setUp(self):
        # Create some sample heroes
        self.chad = Hero("Chad", 27, ["flight", "flame"])
        self.courtney = Hero("Courtney", 20, ["invisibility"])
        self.heroes = [self.chad, self.courtney]

        # Sample emergencies
        self.fire = Emergencies("A raging fire!", "flame", 1)
        self.invisible_thief = Emergencies("Steal attempt!", "invisibility", 1)

        # Create a level
        self.level = Level("Test Level", "Testing automatic play.", [self.fire, self.invisible_thief])

    def test_json_save_load(self):
        save_game(self.heroes, "test_save.json")
        loaded = load_game("test_save.json")
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].name, "Chad")
        os.remove("savefile.json")  # cleanup

    def test_automatic_play(self):
        # Play the level automatically
        self.level.play(self.heroes)
        # Check that at least one hero leveled up
        leveled_up = any(
            getattr(hero, attr) > 1
            for hero in self.heroes
            for attr in ["combat", "vigor", "mobility", "charisma", "intellect"]
        )
        self.assertTrue(leveled_up)

if __name__ == "__main__":
    unittest.main()
