class Player:
    def __init__(self, name, pokémon = []):
        self.name = name
        self.pokémon = pokémon
        self.badges = []
        self.bag = {}
        self.money = 0

    def add_pokémon(self, mon):
        if (len(self.pokémon) < 6):
            self.pokémon.append(mon)
            print(f'{mon} was added to party!')
        else:
            print(f"""You already have six Pokémon:\n
                  {self.pokémon[0]}\n{self.pokémon[1]}\n{self.pokémon[2]}\n
                  {self.pokémon[3]}\n{self.pokémon[4]}\n{self.pokémon[5]}\n
                  {mon} was sent to pc!
                 """)