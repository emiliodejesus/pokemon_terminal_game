import stat_dex
import attack_dex

class Pokémon:
    # To create a pokemon, give it a name, type, and level. Its max health is determined by its level. Its starting health is its max health and it is not knocked out when it starts.

    def __init__(self, name, type, species, level = 5):
        self.name = name
        self.level = level
        self.species = species
        self.type = type
        self.attacks = attack_dex.pokémon_attacks.get(self.species)
        self.is_knocked_out = False
        keys = ['hp', 'att', 'def', 'spA', 'spD', 'spd']
        values = [2*stat_dex.pokémon_stats.get(species)[0] * (level/100) + 10 + self.level]
        for i in range(1, len(keys)):
            values.append(2 * stat_dex.pokémon_stats.get(species)[i] * level)
        self.stats = dict(zip(keys, values))
        self.remaining_hp = self.stats.get('hp')


    def __repr__(self):
        # Printing a pokemon will tell you its name, its type, its level and how much health it has remaining
        return f"This is a level {self.level} {self.species}, has {self.stats.get('hp')} remaining hp. {self.species} are {self.type} type Pokémon."

    def revive(self):
        # Reviving a pokemon will flip it's status to False
        self.is_knocked_out = False
        # A revived pokemon can't have 0 health. This is a safety precaution. revive() should only be called if the pokemon was given some health, but if it somehow has no health, its health gets set to 1.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def knock_out(self):
        # Knocking out a pokemon will flip its status to True.
        self.is_knocked_out = True
        # A knocked out pokemon can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the pokemon had health left, it gets set to 0.
        if self.health != 0:
            self.health = 0
        print("{name} was knocked out!".format(name = self.name))

    def lose_health(self, amount):
        # Deducts heath from a pokemon and prints the current health reamining
        self.health -= amount
        if self.health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the pokemon.
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def gain_health(self, amount):
        # Adds to a pokemon's heath
        # If a pokemon goes from 0 heath, then revive it
        if self.health == 0:
            self.revive()
        self.health += amount
        # Makes sure the heath does not go over the max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def attack(self, attack, other_pokemon):
        # Typing effectiveness
        type_advantage = {
           'normal': [],
           'fire': ['grass', 'ice', 'bug'],
           'water': ['fire', 'ground', 'rock'],
           'electric': ['water', 'flying'],
           'grass': ['water', 'ground', 'rock'],
           'ice': ['grass', 'flying', 'dragon'],
           'fighting': ['normal', 'ice', 'bug'],
           'poison': ['bug', 'grass'],
           'ground': ['fire', 'electric', 'poison', 'rock'],
           'flying': ['grass', 'fighting', 'bug'],
           'psychic': ['fighting', 'poison'],
           'bug': ['grass', 'poison', 'psychic'],
           'rock': ['fire', 'ice', 'flying', 'bug'],
           'ghost': ['ghost'],
           'dragon': ['dragon']
        }
        type_disadvantage = {
           'normal': ['rock'],
           'fire': ['fire', 'water', 'rock', 'water'],
           'water': ['water', 'grass', 'dragon'],
           'electric': ['electric', 'grass', 'dragon'],
           'grass': ['fire', 'grass', 'poison', 'flying', 'bug', 'dragon'],
           'ice': ['water', 'ice'],
           'fighting': ['poison', 'flying', 'psychic', 'bug'],
           'poison': ['poison', 'ground', 'rock', 'ghost'],
           'ground': ['grass', 'bug'],
           'flying': ['electric', 'bug'],
           'psychic': ['psychic'],
           'bug': ['fire', 'fighting', 'flying', 'ghost'],
           'rock': ['fighting', 'ground'],
           'ghost': [],
           'dragon': []
        }
        type_ineffectiveness = {
           'normal': ['ghost'],
           'fire': [],
           'water': [],
           'electric': ['ground'],
           'grass': [],
           'ice': [],
           'fighting': ['ghost'],
           'poison': [],
           'ground': ['flying'],
           'flying': [],
           'psychic': [],
           'bug': [],
           'rock': [],
           'ghost': [],
           'dragon': []
        }

        # Checks to make sure the pokemon isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because it is knocked out!".format(name = self.name))
            return
        # If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
        if(other_pokemon.type in type_advantage.get(self.type)):
           other_pokemon.lose_health(attack * 2)




